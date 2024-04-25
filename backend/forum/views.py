import json
from django.http import JsonResponse
from forum.models import Forum
from members.models import Parent, Trainer
from members.utils import decodeJWT


def loadMessages(request):
    if request.method == "POST":

        return JsonResponse({"error": ""})


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
                    if trainer["rol"] == "parent":
                        parent = Parent.objects.get(user_id=payload["id"])
                        team = parent.trainer.team
                    message = Forum.objects.create(
                        team=team,
                        message=data["message"],
                    )
                    data = message.message
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
