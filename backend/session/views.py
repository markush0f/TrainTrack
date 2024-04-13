from django.http import JsonResponse
from rest_framework import viewsets
from .models import Events, Calendar
import json
from members.utils import decodeJWT
from members.models import *
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = Events


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
            message = Events.objects.create(
                title=data["title"],
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
            return JsonResponse({"error": str(e)}, status=500)
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
                        session = Events.objects.create(
                            title=title,
                            session_description=session,
                            player_id=data["player_id"],
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
                return JsonResponse({"error": str(e)}, status=500)
        else:
            return JsonResponse({"error": "Token JWT no válido o ausente"}, status=401)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
# Enviar aviso de padre a entrenador
def sendNotice(request):

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

            session = Events.objects.create(
                notification=message,
                title=title,
                # notification_create
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
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Error de método  "})


# Lista de mensajes del entrenador
def listNotifications(request):
    if request.method == "GET":
        payload = decodeJWT(request)
        if payload["rol"] == "trainer":
            try:
                trainer = Trainer.objects.get(user_id=payload["user_id"])
                notifications = Events.objects.filter(trainer_id=trainer.id)
                data = []
                for notification in notifications:
                    if notification.title and notification.notification:
                        data.append(
                            {
                                "id": notification.id,
                                "title": notification.title,
                                "notification": notification.notification,
                                "created_at": notification.created_at,
                            }
                        )
                return JsonResponse({"notifications": data})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)
        else:
            return JsonResponse({"error": "Acceso no autorizado"}, status=403)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)


# Mostramos las sesiones o mensajes enviados de entrenador a padre
@csrf_exempt
def listSessions(request):
    if request.method == "GET":
        payload = decodeJWT(request)
        if payload["rol"] == "parent":
            try:
                payload = decodeJWT(request)
                parent = Parent.objects.filter(user_id=payload["user_id"]).first()
                player = Player.objects.filter(parent=parent.id).first()
                sessions = Events.objects.filter(player_id=player.id)
                data = []
                for session in sessions:
                    if session.title and session.session_description:
                        data.append(
                            {
                                "id": session.id,
                                "title": session.title,
                                "session": session.session_description,
                                "created_at": session.created_at,
                            }
                        )
                if data:
                    return JsonResponse({"sessions": data}, status=200)
                else:
                    return JsonResponse({"none": "No hay sessiones"})
            except Exception as e:
                return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "No tiene autorización."}, status=403)


@csrf_exempt
def removeNotification(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            payload = decodeJWT(request)
            if payload["rol"] == "trainer" or payload["rol"] == "parent":
                notification = Events.objects.filter(id=data.get("id")).first()
                if notification:
                    notification.delete()
                    return JsonResponse({"success": "Evento eliminada."})
                else:
                    return JsonResponse({"error": "El evento no existe."}, status=404)
            else:
                return JsonResponse(
                    {"error": "No tienes permisos para realizar esta acción."},
                    status=403,
                )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Datos JSON no válidos."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Método no permitido."}, status=405)


@csrf_exempt
def loadEventsCalendar(request):
    if request.method == "GET":
        try:
            payload = decodeJWT(request)
            if payload:
                parent = Parent.objects.get(user_id=payload["user_id"])
                events = Calendar.objects.filter(team=parent.trainer.team)
                print("EVENTOS:", events)
                eventsData = []
                for event in events:
                    eventsData.append(
                        {
                            "id": event.id,
                            "title": event.title_event,
                            "description": event.description_event,
                            "dateEvent": event.event_date,
                            "dateTime": event.event_time,
                        }
                    )
                if eventsData:
                    return JsonResponse({"events": eventsData}, status=200)
                else:
                    return JsonResponse({"empty": "No hay eventos"})
            else:
                return JsonResponse({"error": "No tiene autorización"}, status=403)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Metodo no permitido"}, status=405)
