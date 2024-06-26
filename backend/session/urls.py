from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("sessions", views.SessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "trainer/messages/listnotifications",
        views.listNotifications,
        name="listNotifications",
    ),
    path("trainer/sendsession", views.writeSession, name="sendsession"),
    path("parent/sendnotification", views.writeNotification, name="sendnotification"),
    path("parent/sendnotice", views.sendNotification, name="sendnotices"),
    # Ruta para eliminar notificaciónada
    path(
        "removenotification",
        views.removeNotification,
        name="remove_notification",
    ),
    path("parent/listsessions", views.listSessions, name="listSessions"),
    # Ruta para devolver todos los eventos
    path("calendar/events", views.loadEventsCalendar, name="loadevents"),
    # Ruta para crear un nuevo evento
    path("calendar/events/createevent", views.createEvent, name="createevent"),
    # Ruta para eliminar un evento
    path("calendar/events/removeevent", views.removeEvent, name="createevent"),
]
