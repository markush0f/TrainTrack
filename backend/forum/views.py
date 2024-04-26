import json
from django.http import JsonResponse
from forum.models import Forum
from members.models import Parent, Trainer
from members.utils import decodeJWT


def loadMessages(request):
    if request.method == "GET":
        try:
            payload = decodeJWT(request)
            if payload:
                user_id = payload["user_id"]
                rol = payload["rol"]
                if rol == "parent":
                    parent = Parent.objects.get(user_id=user_id)
                    forum = Forum.objects.filter(team=parent.trainer.team)
                elif rol == "trainer":
                    trainer = Trainer.objects.get(user_id=user_id)
                    forum = Forum.objects.filter(team=trainer.team)
                else:
                    return JsonResponse({"error": "Rol no reconocido"}, status=400)

                data = [
                    {
                        "id": message.id,
                        "title": message.title,
                        "message": message.message,
                        "author": message.author,
                    }
                    for message in forum
                ]
                print(data)
                if data:
                    return JsonResponse({"events": data}, status=200)
                else:
                    return JsonResponse({"empty": "No hay mensajes en el foro"})
            else:
                return JsonResponse({"error": "No tiene autorización"}, status=403)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)


def sendMessage(request):
    if request.method == "POST":
        try:
            payload = decodeJWT(request)
            if payload:
                data = json.loads(request.body)
                if data:
                    if payload["rol"] == "trainer":
                        trainer = Trainer.objects.get(user_id=payload["id"])
                        team = trainer.team
                        author = trainer.user.first_name
                    if trainer["rol"] == "parent":
                        parent = Parent.objects.get(user_id=payload["id"])
                        team = parent.trainer.team
                        author = parent.user.first_name
                    message = Forum.objects.create(
                        team=team,
                        message=data["message"],
                        title=data["title"],
                        author=author,
                    )
                    data = {
                        'team': message.team,
                        'message': message.message,
                        'title': message.title,
                        'author': message.author
                    }
                    if message:
                        return JsonResponse(
                            {"success": "true", "message": data}, status=200
                        )
                    if not parent:
                        return JsonResponse({"error": "User not found"}, status=404)

            else:
                return JsonResponse({"error": "Bad request"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)})
