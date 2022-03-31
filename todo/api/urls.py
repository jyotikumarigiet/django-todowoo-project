from django.urls import path, include
from rest_framework import urlpatterns
from todo.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todoapi', views.TodoViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls))
]