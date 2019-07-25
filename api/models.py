from django.db import models


class Task(models.Model):
    """
    Задача
    """
    INQUEUE = 'In Queue'
    RUN = 'Run'
    COMPLETED = 'Completed'

    STATUS_CHOICES = [
        (INQUEUE, 'Задача ждёт своей очереди на выполнение'),
        (RUN, 'Произошел запуск задачи'),
        (COMPLETED, 'Задача выполнена'),
    ]
    id = models.AutoField(
        'Номер поставленной задачи',
        primary_key=True,
    )
    status = models.CharField(
        'Статус задачи',
        max_length=100,
        choices=STATUS_CHOICES,
        default='In Queue',
    )
    create_time = models.DateTimeField(
        'Время создания задачи',
        auto_now_add=True,
        blank=True,
    )
    start_time = models.DateTimeField(
        'Время старта задачи',
        null=True,
        blank=True,
    )
    exec_time = models.DurationField(
        'Время выполнения задачи',
        null=True,
        blank=True,
    )
