from django.http import JsonResponse
from rest_framework import viewsets
from .models import Message
import json
from members.utils import verifyToken, decodeJWT
from members.models import *


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = Message


# Mensaje de padre al entrenador
def writeNotification(request):
    if request.method == "POST":
        payload = decodeJWT(request)
        data = json.loads(request.body)
        parent_id = payload["user_id"]
        message = Message.objects.create(
            notfication_tittle=data["tittle"],
            notfication=data["notification"],
            player_id=data[""],
        )
        parent = Parent.objects.get(id=payload["user_id"])


# Lista de mensajes del entrenador
def listNotifications(request):
    if request.method == "GET":
        payload = decodeJWT(request)
        if payload["rol"] == "trainer":
            try:
                notifications = Message.objects.filter(trainer_id=payload["user_id"])
                data = [
                    {
                        "title": notification.notification_title,
                        "notification": notification.notification,
                    }
                    for notification in notifications
                ]
                return JsonResponse({"notifications": data})
            except Exception as e:
                print("Error:", e)
                return JsonResponse(
                    {"error": "Error al recuperar las notificaciones"}, status=500
                )
        else:
            return JsonResponse({"error": "Acceso no autorizado"}, status=403)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
