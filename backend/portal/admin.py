from django.contrib import admin
from .models import Course, Schedule, Grade, Assignment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'teacher', 'credits', 'created_at']
    search_fields = ['title', 'teacher']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'day', 'start_time', 'end_time', 'room']
    list_filter = ['day', 'course']


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'course', 'score', 'graded_at']
    list_filter = ['course']


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'course', 'author', 'status', 'due_date', 'created_at']
    list_filter = ['status', 'course']
    search_fields = ['title']