from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Course, Schedule, Grade, Assignment

class RegisterSerializer(serializers.Serializer):
    """Сериализатор регистрации — чистый Serializer."""
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, min_length=6)
    email = serializers.EmailField(required=False, allow_blank=True)
    first_name = serializers.CharField(max_length=150, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=150, required=False, allow_blank=True)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Пользователь с таким именем уже существует.')
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        return user


class GradeSerializer(serializers.Serializer):
    """Сериализатор оценок — чистый Serializer."""
    id = serializers.IntegerField(read_only=True)
    course_id = serializers.IntegerField()
    course_title = serializers.SerializerMethodField()
    score = serializers.DecimalField(max_digits=5, decimal_places=2)
    comment = serializers.CharField(allow_blank=True, required=False)
    graded_at = serializers.DateTimeField(read_only=True)

    def get_course_title(self, obj):
        return obj.course.title

    def validate_score(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError('Оценка должна быть от 0 до 100.')
        return value

    def validate_course_id(self, value):
        from .models import Course
        if not Course.objects.filter(id=value).exists():
            raise serializers.ValidationError('Курс с таким ID не найден.')
        return value

    def create(self, validated_data):
        return Grade.objects.create(**validated_data)

