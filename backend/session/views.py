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
    # if request.method != "POST":
    #     return JsonResponse({"error": "Método no permitido"}, status=405)

    if request.method == "POST":
        payload = decodeJWT(request)

        if not payload:
            return JsonResponse({"error": "Token no válido"}, status=400)

        try:
            data = json.loads(request.body)
            notice_type = data["notice"]

            if not notice_type:
                return JsonResponse({"error": "Debe enviar una noticia"}, status=400)

            # LOGICA PARA QUE SOLO SE ENVIE EL MENSAJE DEL HIJO, GUARDARLO EN EL TOKEN.
            parent = Parent.objects.get(user_id=payload["user_id"])
            player = Player.objects.filter(parent_id=parent.id).first()

            notifications = {
                "notNextTrain": (
                    "Asistencia a entrenamiento",
                    f"{player.name} no podrá acudir al siguiente entrenamiento",
                ),
                "notNextMatch": (
                    "Asistencia a partido",
                    f"{player.name} no podrá acudir al siguiente partido",
                ),
                "lateNextTrain": (
                    "Asistencia a entrenamiento",
                    f"{player.name} acudirá tarde al siguiente entrenamiento",
                ),
                "lateNextMatch": (
                    "Asistencia a partido",
                    f"{player.name} acudirá tarde al siguiente partido",
                ),
            }

            if notice_type not in notifications:
                return JsonResponse(
                    {"error": "Tipo de notificación no válido"}, status=400
                )

            title, message = notifications[notice_type]

            session = Message.objects.create(
                notification=message,
                notification_title=title,
                player_id=player.id,
                trainer_id=parent.trainer_id,
            )

            if session:
                return JsonResponse({"success": True, "notice": message})
        except Parent.DoesNotExist:
            return JsonResponse(
                {"error": "No se encontró ningún padre con el ID proporcionado"},
                status=404,
            )
        except Player.DoesNotExist:
            return JsonResponse(
                {"error": "No se encontró ningún jugador asociado al padre"}, status=404
            )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Datos JSON no válidos"}, status=400)
        except Exception as e:
            print("Error:", e)
            return JsonResponse({"error": "Error al crear la notificación"}, status=500)
    else:
        return JsonResponse({"error": "Error desconocido"}, status=500)


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
