from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import redirect
import json
from forms import SignupForm
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


#  Comprobamos si en los datos enviados existe tanto el codigo como la contraseña proporcionada por el equipo
#  La idea es que cada mes se cambie tanto el codigo como la contraseña del equipo
# Añadir esta funcion para que pase primero por forms.py
@csrf_exempt
def checkCodeTeam(request):
    if request.method == "POST":
        print("REQUESTR :", request)
        # Obtenemos el code_team y la password del equipo, y luego el entrenador debe aceptar al padre
        data = json.loads(request.body)
        print(data["password"])
        if data["codeTeam"] and data["password"]:
            try:
                codeTeam = Team.objects.all().filter(team_code=data["codeTeam"])
                password = Team.objects.all().filter(team_password=data["password"])
                if password and codeTeam:
                    print("Parametros correctos")
                    return JsonResponse(
                        {
                            "redirect": "http://localhost:5173/signup",
                            "success": "Datos correctos",
                        }
                    )
                else:
                    return JsonResponse(
                        {"error": "Contraseña o código de equipo incorrecto"},
                        safe=False,
                        status=400,
                    )
            except Exception as e:
                return JsonResponse({"error": e}, status=400)
# PONER UNA SEGUNDA CONTRASEÑA
# Cambiar el csrf, esto hace que el navegador ignore el csrf

@csrf_exempt
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST) # Recogemos los datos del formulario
        # Comprobamos si el formulario recodigo es valido
        if form.is_valid():     
            email = form.cleaned_data['email']
            return JsonResponse({"success": "Registrado con éxito"}, status=200)
        else:
            errors = form.errors
            return JsonResponse({"error": errors}, status=400)
    else:
        return JsonResponse({"error": "Debe utilizar un método POST"}, status=405)
