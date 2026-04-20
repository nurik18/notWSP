from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import Course, Schedule, Grade, Assignment
from .serializers import (
    RegisterSerializer,
    GradeSerializer,
    CourseModelSerializer,
    ScheduleModelSerializer,
    AssignmentModelSerializer,
)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """
    FBV. Регистрация нового пользователя.
    POST /api/auth/register/
    """
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                'message': 'Регистрация прошла успешно.',
                'token': token.key,
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                },
            },
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    FBV. Вход в систему — возвращает токен.
    POST /api/auth/login/
    """
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response(
            {'error': 'Необходимо указать username и password.'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user = authenticate(username=username, password=password)
    if user is None:
        return Response(
            {'error': 'Неверные учётные данные.'},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    token, _ = Token.objects.get_or_create(user=user)
    return Response(
        {
            'token': token.key,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            },
        }
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """
    FBV. Выход — удаляет токен пользователя.
    POST /api/auth/logout/
    """
    request.user.auth_token.delete()
    return Response({'message': 'Вы вышли из системы.'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def course_list_view(request):
    """
    FBV #1. Список всех курсов.
    GET /api/courses/
    """
    courses = Course.objects.all()
    serializer = CourseModelSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def schedule_list_view(request):
    """
    FBV #2. Список расписания. Можно фильтровать по ?course_id=1
    GET /api/schedule/
    GET /api/schedule/?course_id=1
    """
    schedules = Schedule.objects.select_related('course').all()

    course_id = request.query_params.get('course_id')
    if course_id:
        schedules = schedules.filter(course_id=course_id)

    serializer = ScheduleModelSerializer(schedules, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def grade_list_view(request):
    """
    FBV. Оценки текущего студента.
    GET  /api/grades/   — список своих оценок
    POST /api/grades/   — добавить оценку (для тестирования)
    """
    if request.method == 'GET':
        # Студент видит только свои оценки
        grades = Grade.objects.filter(student=request.user).select_related('course')
        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            grade = Grade.objects.create(
                student=request.user,
                course_id=serializer.validated_data['course_id'],
                score=serializer.validated_data['score'],
                comment=serializer.validated_data.get('comment', ''),
            )
            result = GradeSerializer(grade)
            return Response(result.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def grade_list_view(request):
    """
    FBV. Оценки текущего студента.
    GET  /api/grades/   — список своих оценок
    POST /api/grades/   — добавить оценку (для тестирования)
    """
    if request.method == 'GET':
        # Студент видит только свои оценки
        grades = Grade.objects.filter(student=request.user).select_related('course')
        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            grade = Grade.objects.create(
                student=request.user,
                course_id=serializer.validated_data['course_id'],
                score=serializer.validated_data['score'],
                comment=serializer.validated_data.get('comment', ''),
            )
            result = GradeSerializer(grade)
            return Response(result.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AssignmentListCreateAPIView(APIView):
    """
    CBV #1 на APIView. Список заданий и создание нового.
    GET  /api/assignments/
    POST /api/assignments/
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Возвращает задания текущего пользователя."""
        assignments = Assignment.objects.filter(
            author=request.user
        ).select_related('course', 'author')
        serializer = AssignmentModelSerializer(assignments, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Создаёт задание. Автор берётся из request.user."""
        serializer = AssignmentModelSerializer(data=request.data)
        if serializer.is_valid():
            assignment = serializer.save(author=request.user)
            return Response(
                AssignmentModelSerializer(assignment).data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AssignmentDetailAPIView(APIView):
    """
    CBV #2 на APIView. Операции с конкретным заданием.
    GET    /api/assignments/<pk>/
    PUT    /api/assignments/<pk>/
    DELETE /api/assignments/<pk>/
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        """Вспомогательный метод: получить задание или вернуть None."""
        try:
            return Assignment.objects.get(pk=pk)
        except Assignment.DoesNotExist:
            return None

    def get(self, request, pk):
        assignment = self.get_object(pk, request.user)
        if assignment is None:
            return Response(
                {'error': 'Задание не найдено.'},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = AssignmentModelSerializer(assignment)
        return Response(serializer.data)

    def put(self, request, pk):
        assignment = self.get_object(pk, request.user)
        if assignment is None:
            return Response(
                {'error': 'Задание не найдено.'},
                status=status.HTTP_404_NOT_FOUND,
            )
        # Только автор может редактировать
        if assignment.author != request.user:
            return Response(
                {'error': 'Вы не являетесь автором этого задания.'},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = AssignmentModelSerializer(
            assignment, data=request.data, partial=False
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        assignment = self.get_object(pk, request.user)
        if assignment is None:
            return Response(
                {'error': 'Задание не найдено.'},
                status=status.HTTP_404_NOT_FOUND,
            )
        # Только автор может удалять
        if assignment.author != request.user:
            return Response(
                {'error': 'Вы не являетесь автором этого задания.'},
                status=status.HTTP_403_FORBIDDEN,
            )
        assignment.delete()
        return Response(
            {'message': 'Задание удалено.'},
            status=status.HTTP_204_NO_CONTENT,
        )
