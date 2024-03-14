from django.http import JsonResponse
from rest_framework import viewsets
from .models import Message
import json
from members.utils import verifyToken, decodeJWT
from members.models import *
from django.views.decorators.csrf import csrf_exempt


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = Message


# Mensaje de padre al entrenador
def writeNotification(request):
    if request.method == "POST":
        payload = decodeJWT(request)
        data = json.loads(request.body)
        parent = Parent.objects.get(user_id=payload["user_id"])
        message = Message.objects.create(
            notfication_tittle=data["tittle"],
            notfication=data["notification"],
            player_id=data[""],
        )
        parent = Parent.objects.get(id=payload["user_id"])


# Sesión de entrenador al padre
@csrf_exempt
def writeSession(request):
    if request.method == "POST":
        payload = decodeJWT(request)
        if payload:
            data = json.loads(request.body)
            try:
                title = data["title"]
                session = data["session"]
                if title and session:
                    trainer = Trainer.objects.get(user_id=payload["user_id"])
                    if trainer:
                        session = Message.objects.create(
                            session_title=title,
                            session_description=session,
                            player_id=1,
                            trainer_id=trainer.id,
                        )
                        return JsonResponse({"success": "Sesión creada"})
                    else:
                        return JsonResponse(
                            {"error": "No se encontró ningún entrenador"}, status=400
                        )
                else:
                    return JsonResponse(
                        {
                            "error": "Faltan campos obligatorios en los datos de la solicitud"
                        },
                        status=400,
                    )
            except Exception as e:
                print("Error:", e)
                return JsonResponse({"error": "Error al crear la sesión"}, status=500)
        else:
            return JsonResponse({"error": "Token JWT no válido o ausente"}, status=401)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)


# Lista de mensajes del entrenador
def listNotifications(request):
    if request.method == "POST":
        payload = decodeJWT(request)
        if payload["rol"] == "trainer":
            try:
                trainer = Trainer.objects.get(user_id=payload["user_id"])
                notifications = Message.objects.filter(trainer_id=trainer.id)
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
