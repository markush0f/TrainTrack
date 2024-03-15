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
@csrf_exempt
def writeNotification(request):
    # Verificar el rol de padre
    if request.method == "POST":
        payload = decodeJWT(request)
        data = json.loads(request.body)
        try:
            parent = Parent.objects.get(user_id=payload["user_id"])
            player = Player.objects.get(parent_id=parent.id)
            message = Message.objects.create(
                notification_title=data["title"],
                notification=data["notification"],
                player_id=player.id,
            )
            return JsonResponse({"success": True, "parent": parent.id})
        except Parent.DoesNotExist:
            return JsonResponse(
                {"error": "No se encontró ningún padre con el ID proporcionado"},
                status=404,
            )
        except Exception as e:
            print("Error:", e)
            return JsonResponse({"error": "Error al crear la notificación"}, status=500)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)


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


@csrf_exempt
# Enviar aviso de padre a entrenador
def sendNotice(request):
    if request.method == "POST":
        payload = verifyToken(request)
        if payload:
            data = json.loads(request.body)
            try:
                notice_type = data.get("title")
                if notice_type:
                    parent = Parent.objects.get(id=payload["user_id"])
                    player = Player.objects.get(parent_id=parent.id)
                    new_title = ""
                    new_notice = ""
                    if notice_type == "notNextTrain":
                        new_title = "Asistencia a entrenamiento"
                        new_notice = (
                            f"{player.name} no podrá acudir al siguiente entrenamiento"
                        )
                    elif notice_type == "notNextMatch":
                        new_title = "Asistencia a partido"
                        new_notice = (
                            f"{player.name} no podrá acudir al siguiente partido"
                        )
                    elif notice_type == "lateNextTrain":
                        new_title = "Asistencia a entrenamiento"
                        new_notice = (
                            f"{player.name} acudirá tarde al siguiente entrenamiento"
                        )
                    elif notice_type == "lateNextMatch":
                        new_title = "Asistencia a partido"
                        new_notice = f"{player.name} acudirá tarde al siguiente partido"
                    else:
                        return JsonResponse(
                            {"error": "Tipo de notificación no válido"}, status=400
                        )

                    session = Message.objects.create(
                        notification=new_notice,
                        notification_title=new_title,
                        player_id=player.id,
                        trainer_id=parent.trainer_id,
                    )
                    if session:
                        return JsonResponse({"success": True})
                else:
                    return JsonResponse(
                        {"error": "Falta el campo 'title' en los datos"}, status=400
                    )
            except Parent.DoesNotExist:
                return JsonResponse(
                    {"error": "No se encontró ningún padre con el ID proporcionado"},
                    status=404,
                )
            except Player.DoesNotExist:
                return JsonResponse(
                    {"error": "No se encontró ningún jugador asociado al padre"},
                    status=404,
                )
            except Exception as e:
                print("Error:", e)
                return JsonResponse(
                    {"error": "Error al crear la notificación"}, status=500
                )
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)


# Lista de mensajes del entrenador
def listNotifications(request):
    if request.method == "GET":
        payload = decodeJWT(request)
        if payload["rol"] == "trainer":
            try:
                trainer = Trainer.objects.get(user_id=payload["user_id"])
                notifications = Message.objects.filter(trainer_id=trainer.id)
                data = []
                for notification in notifications:
                    if notification.notification_title and notification.notification:
                        data.append(
                            {
                                "title": notification.notification_title,
                                "notification": notification.notification,
                            }
                        )
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
