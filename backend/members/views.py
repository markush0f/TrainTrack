from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import redirect
import json
from .models import *
from .serializers import *

user_manager = CustomUserManager()


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
                if not codeTeam:
                    print("Codigo no encontrado")
                    return JsonResponse("Código de equipo incorrecto", safe=False)
                else:
                    print("codigo encontrado", codeTeam)
                if password and codeTeam:
                    print("Contraseña correcta")
                    return JsonResponse(
                        {
                            "redirect": "http://localhost:5173/signup",
                            "success": "Contraseña correcta",
                        }
                    )
                else:
                    print("Contraseña incorrecta")
                    return JsonResponse("Contraseña incorrecta", safe=False)
            except NameError:
                print("Error:", NameError)




# Poner dos password
def SignUpTrainer(request):
    name = request.POST.get("name")
    surname = request.POST.get("surname")
    email = request.POST.get("email")
    birth = request.POST.get("birth")
    password = request.POST.get("password")
    dni = request.POST.get("dni")
    address1 = request.POST.get("address1")
    address2 = request.POST.get("address2")
    phone = request.POST.get("phone")

    result = user_manager.create_trainer(
        name=name, surname=surname, email=email, birth=birth, password=password
    )
    if isinstance(result, dict):
        return JsonResponse(result, dict)
    else:
        return JsonResponse({"success": "Entrenador creado correctamente"})
