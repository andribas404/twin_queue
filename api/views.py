from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для отображения задач.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
