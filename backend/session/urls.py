from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("sessions", views.SessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("trainer/messages/listnotifications", views.listNotifications, name="listNotifications"),
]
