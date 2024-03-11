from . import views
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("teams", TeamViewSet, basename="teams")


