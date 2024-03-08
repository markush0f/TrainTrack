from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
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
from .forms import TrainerForm
from django.contrib.auth import authenticate, login


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
                    print("Contraseña incorrecta")
                    return JsonResponse("Contraseña incorrecta", safe=False)
            except NameError:
                print("Error:", NameError)


# Con autenticación
@csrf_exempt
def SignUpTrainer(request):
    if request.method == "POST":
        data = json.loads(request.body)
        errors = {}
        # Comprobamos si ya existe en la tabla User el email
        for key, value in data.items():
            if not value:
                errors[f"{key}Empty"] =f"El campo {key} no puede estar vacio"
            print(f"Key: {key}, Value: {value}")
        if errors:
            return JsonResponse({"Errors:": errors}, safe=False)
        # if User.objects.filter(email=email).exists():
        #     return JsonResponse(
        #         {"errors": "Este correo electrónico ya está registrado."},
        #         status=400,
        #     )
    #     # Creamos el usuario
    #     try:
    #         user = User.objects.create_user(
    #             email, email, password, first_name=first_name, last_name=last_name
    #         )
    #     except Exception as e:
    #         return JsonResponse({"errors": e}, status=500)
    #     # Autenticamos el usuario
    #     if user is not None:
    #         # Creamos al entrenador
    #         trainer = createTrainer(form.cleaned_data, user)
    #         login(request, user)
    #         return JsonResponse(
    #             {"success": "El entrenador ha sido autenticado y creado."},
    #             status=200,
    #         )
    #     return JsonResponse(
    #         {"error": "No se ha podido autenticar el entrenador."}, status=500
    #     )
    # else:
    #     return JsonResponse({"errors": form.errors}, status=400)


# Creamos el entrenador
def createTrainer(data, user):
    trainer = Trainer.objects.create(
        user=user,
        birth=data["birth"],
        dni=data["dni"],
        address1=data["address1"],
        address2=data.get("address2", ""),
        phone=data["phone"],
    )
    return trainer
