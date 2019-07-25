from datetime import datetime, timezone

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer
from .tasks import task_run


class TaskViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для отображения задач.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(methods=['post'], detail=False, url_path='create', url_name='create')
    def create_task(self, request, format=None):
        """
        Создание задачи
        create/
        """
        task = Task()
        task.save()
        task_run.delay(task.pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    @action(methods=['post'], detail=True, url_path='start', url_name='start')
    def start_task(self, request, pk=None, format=None):
        """
        Запуск задачи
        <pk>/start/
        """
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=404,
                            data=dict(details='Задачи с таким номером не существует'))
        if task.status != Task.INQUEUE:
            return Response(status=400,
                            data=dict(details='Задача уже была запущена'))
        task.status = Task.RUN
        task.start_time = datetime.now()
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    @action(methods=['post'], detail=True, url_path='complete', url_name='complete')
    def complete_task(self, request, pk=None, format=None):
        """
        Завершение задачи
        <pk>/complete/
        """
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=404,
                            data=dict(details='Задачи с таким номером не существует'))
        if task.status != Task.RUN:
            return Response(status=400,
                            data=dict(details='Задача не может быть завершена'))
        task.status = Task.COMPLETED
        now = datetime.now(timezone.utc)
        task.exec_time = now - task.start_time
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data)
