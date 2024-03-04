from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
import json
# viewsets es una clase que combina las funciones de varias
# vistas genéricas para proporcionar un conjunto
# completo de operaciones CRUD para un modelo especifico

from .models import *
from .serializers import *


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

    # Filtramos por equipo:
    @action(detail=False)
    def by_team(self, request):
        team = self.request.query_params.get("team", None)
        trainer = Trainer.objects.filter(team=team)
        serializer = TrainerSerializer(trainer, many=True)
        # http://127.0.0.1:8000/api/trainers/by_team/?team=1
        return Response(serializer.data)


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


# Cambiar el csrf, esto hace que el navegador ignore el csrf
@csrf_exempt
def signup(request):
    # Creamos un Padre
    if request.method == "POST":
        data = json.loads(request.body) # Recoge los datos enviados, mediante jsonj
        print("Request", request)
        print("Name: ", data.get("Name"))
    return JsonResponse(data, safe=False)


# def loginParent(request):s
#     if request.method == "POST":
#         if request.user.is_authenticated:
#             print("Inicio sesión")
