import json
from django.http import JsonResponse
from forum.models import Forum
from members.models import Parent, Trainer
from members.utils import decodeJWT
from django.views.decorators.csrf import csrf_exempt


def loadMessages(request):
    if request.method == "GET":
        try:
            payload = decodeJWT(request)
            if payload:
                print(payload)
                user_id = payload["user_id"]
                rol = payload["rol"]
                if rol == "parent":
                    parent = Parent.objects.get(user_id=user_id)
                    forum = Forum.objects.filter(team=parent.trainer.team)
                elif rol == "trainer":
                    trainer = Trainer.objects.get(user_id=user_id)
                    forum = Forum.objects.filter(team=trainer.team)
                else:
                    return JsonResponse({"error": "No tiene autorización"}, status=403)

                data = [
                    {
                        "id": message.id,
                        "title": message.title,
                        "message": message.message,
                        "author": message.author,
                        'created_at': message.created_at
                    }
                    for message in forum
                ]
                print(data)
                if data:
                    return JsonResponse({"messages": data, "success": True}, status=200)
                else:
                    return JsonResponse({"empty": "No hay mensajes en el foro"})
            else:
                return JsonResponse({"error": "No tiene autorización"}, status=403)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def sendMessage(request):
    if request.method == "POST":
        try:
            payload = decodeJWT(request)
            if payload:
                data = json.loads(request.body)
                print("Entra; ", data)
                if data:
                    if payload["rol"] == "trainer":
                        trainer = Trainer.objects.get(user_id=payload["user_id"])
                        team = trainer.team
                        author = trainer.user.first_name
                    if payload["rol"] == "parent":
                        parent = Parent.objects.get(user_id=payload["user_id"])
                        team = parent.trainer.team
                        author = parent.user.first_name
                        print(team.name)

                    message = Forum.objects.create(
                        team_id=team.id,
                        message=data["message"],
                        title=data["title"],
                        author=author,
                    )
                    print(message)
                    data = {
                        "team": message.team.name,
                        "message": message.message,
                        "title": message.title,
                        "author": message.author,
                    }
                    print("Mensaje: ", data)
                    if message:
                        return JsonResponse(
                            {"success": "true", "message": data}, status=200
                        )
                    if not parent and not trainer:
                        return JsonResponse({"error": "User not found"}, status=404)

            else:
                return JsonResponse({"error": "Bad request"}, status=400)
        except Exception as e:
            print("error: ", str(e))
            return JsonResponse({"error": str(e)})
