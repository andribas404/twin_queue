# -*- coding: utf-8 -*-
from rest_framework import routers

from .views import TaskViewSet

app_name = 'api'
router = routers.SimpleRouter()
router.register('', TaskViewSet, basename='api')
urlpatterns = router.urls
