from django.urls import path
from . import views

urlpatterns = [
    # ── Аутентификация ──
    path('auth/register/', views.register_view, name='register'),
    path('auth/login/', views.login_view, name='login'),
    path('auth/logout/', views.logout_view, name='logout'),

    # ── Курсы (FBV #1) ──
    path('courses/', views.course_list_view, name='course-list'),

    # ── Расписание (FBV #2) ──
    path('schedule/', views.schedule_list_view, name='schedule-list'),

    # ── Оценки (FBV) ──
    path('grades/', views.grade_list_view, name='grade-list'),

    # ── Задания (CBV APIView) ──
    path('assignments/', views.AssignmentListCreateAPIView.as_view(), name='assignment-list-create'),
    path('assignments/<int:pk>/', views.AssignmentDetailAPIView.as_view(), name='assignment-detail'),
]