from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import redirect
import json
import re

# re es un módulo de expresiones regulares
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


def formErrors(data):
    errors = {}
    onlyTxt = re.compile(r"\d+")
    
    if data:
        if data["name"]:
            name = data["name"]
            if onlyTxt.search(name) or len(name) > 20 or len(name) < 2:
                errors["formatNameIncorrect"] = "Debe introducir un nombre correcto."
        if data["email"]:
            email = data["email"]
            if 
    if errors:
        return errors


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


# MIRAR EL PINIA
# GENERA TOKEN
@csrf_exempt
def signup(request):
    if request.method == "POST":
        data = json.loads(request.body)
        errors = {}
        # Comprobamos si ya existe en la tabla User el email
        for key, value in data.items():
            if not value:
                errors[f"{key}Empty"] = f"El campo {key} no puede estar vacio"
            print(f"Key: {key}, Value: {value}")

        if errors:
            return JsonResponse({"Errors: ": errors})
        # Arreglar esto
        if User.objects.filter(email=data["email"]).exists():
            return JsonResponse(
                {"Error": "Este correo electrónico ya está registrado."}, status=400
            )
        # Creamos el usuario en la base de datos User
        user = createUser(data)
        trainer = createTrainer(data, user.id)
        # Autenticamos el usuario, para así añadir los datos restantes a la tabla entrenador
        if user is not None:
            # Creamos al entrenador
            if trainer:
                return JsonResponse(
                    {"success": "El entrenador ha sido autenticado y creado."},
                    status=201,
                )
        return JsonResponse(
            {"El entrenador no ha sido autenticado ni creado"}, status=500
        )


def createUser(data):
    try:
        user = User.objects.create_user(
            data["email"],
            data["email"],
            data["password"],
            first_name=data["name"],
            last_name=data["surname"],
        )
        return user
    except Exception as e:
        print("116:", e)
        return None


def createTrainer(data, user_id):
    try:
        trainer = Trainer.objects.create(
            user_id=user_id,
            birth=data["birth"],
            address1=data["address1"],
            address2=data["address2"],
            phone=data["phone"],
            team_id=1,
        )
        return trainer
    except Exception as e:
        print("132: ", e)
        return None
