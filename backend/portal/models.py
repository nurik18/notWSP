from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    """Учебный курс."""
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    teacher = models.CharField(max_length=200, verbose_name='Преподаватель')
    credits = models.PositiveIntegerField(default=3, verbose_name='Кредиты')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title


class Schedule(models.Model):
    """Расписание занятий. ForeignKey на Course."""
    DAYS = [
        ('MON', 'Понедельник'),
        ('TUE', 'Вторник'),
        ('WED', 'Среда'),
        ('THU', 'Четверг'),
        ('FRI', 'Пятница'),
        ('SAT', 'Суббота'),
    ]

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='schedules',
        verbose_name='Курс'
    )
    day = models.CharField(max_length=3, choices=DAYS, verbose_name='День недели')
    start_time = models.TimeField(verbose_name='Начало')
    end_time = models.TimeField(verbose_name='Конец')
    room = models.CharField(max_length=50, verbose_name='Аудитория')

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'

    def __str__(self):
        return f'{self.course.title} — {self.get_day_display()} {self.start_time}'


