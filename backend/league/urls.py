from . import views
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("teams", TeamViewSet, basename="teams")

urlpatterns = [
    path("", include(router.urls)),
    path("teams", listTeams, name="list_teams"),
    path("shields", listShields, name="list_shields")
]
