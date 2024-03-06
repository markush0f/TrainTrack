from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import redirect
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


def checkCodeTeam(request):
    if request.method == "POST":
        # Obtenemos el code_team y la password del equipo, y luego el entrenador debe aceptar al padre
        if request.POST["code_team"] and request.POST["password"]:
            try:
                codeTeam = Team.objects.all().filter(code_team=request.POST["code_team"])
                password = Team.objects.all().filter(password=request.POST["password"])
                if codeTeam:
                    print("codigo encontrado", codeTeam)
                else:
                    print("Codigo no encontrado")
                    return JsonResponse("Código de equipo incorrecto", safe=False)
                if password:
                    print("Contraseña correcta")
                else:
                    print("Contraseña incorrecta")
                    return JsonResponse("Contraseña incorrecta", safe=False)
                return redirect(reverse("register")+"?msg=Codigo correcto")
            except NameError:
                print("Error:", NameError)

# Cambiar el csrf, esto hace que el navegador ignore el csrf
@csrf_exempt
def signup(request):
    # Creamos un Padre
    if request.method == "POST":
        # Obtenemos los datos del request
        data = json.loads(request.body)  # Recoge los datos enviados, mediante jsonj
        # Validacion de datos
    return JsonResponse("Entra", safe=False)
