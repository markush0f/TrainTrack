from rest_framework import viewsets
from models import Message
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
            player_id = data['']
        )
        parent = Parent.objects.get(id=payload["user_id"])
