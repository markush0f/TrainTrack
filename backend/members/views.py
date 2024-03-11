from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.decorators import (
    action,
    permission_classes,
    authentication_classes,
    api_view,
)
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from .serializers import *
from django.contrib.auth import authenticate, login
import json, re, jwt
from datetime import datetime, timedelta
from django.conf import settings

# re es un módulo de expresiones regulares
# viewsets es una clase que combina las funciones de varias
# vistas genéricas para proporcionar un conjunto
# completo de operaciones CRUD para un modelo especifico


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

    # Filtramos por equipo:
    # El action crea una ruta personalizada en el enrutador del viewset
    @action(detail=False)
    def by_team(self, request):
        team = self.request.query_params.get("team", None)
        trainer = Trainer.objects.filter(team=team)
        serializer = TrainerSerializer(trainer, many=True)
        # http://127.0.0.1:8000/api/trainers/by_team/?team=1
        return Response(serializer.data)




# class ParentViewSet(viewsets.ModelViewSet):
#     queryset = Team.objects.all()
#     serializer_class = ParentSerializer


# Validamos el token JWT
def verifyToken(request):
    # print(request.headers['Authorization'])
    if request.method == "GET":
        token = request.headers["Authorization"]
        data = json.loads(request.body)
        if token and token.startswith("Bearer ") and data["rol"]:
            print("token recogido y empieza por Bearer")
            print(token)
            # SEGÚN EL ID, ENVIAR EL ROL DE SI ES PADRE O ENTRENADOR
            try:
                tokenJWT = token.split(" ")[1]
                # Decodificamos el token JWT
                payload = jwt.decode(
                    tokenJWT, settings.SECRET_KEY, algorithms=["HS256"]
                )
                print("Payload:", payload)
                return JsonResponse(
                    {
                        "message": "Token válido",
                        "valid": True,
                        "rol": data["rol"],
                    },
                    status=200,
                )
            except Exception as e:
                print("Error: ", e)
        return JsonResponse(
            {
                "message": "Token no válido",
                "error": "Debe iniciar sesión.",
                "valid": False,
            },
            status=200,
        )


# Generamos el token JWT
def generateJWT(user):
    payload = {
        "user_id": user.id,
        # "rol": rol,
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token


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
    if errors:
        return errors


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
                if password and codeTeam:
                    print("Parametros correctos")
                    return JsonResponse(
                        {
                            "redirect": "http://localhost:5173/signup",
                            "success": "Datos correctos",
                        }
                    )
                else:
                    print("Contraseña o código de equipo incorrecto")
                    return JsonResponse("Contraseña incorrecta", safe=False)
            except NameError:
                print("Error:", NameError)


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


def createParent(data, user_id):
    try:
        parent = Parent.objects.create(
            user_id=user_id,
            birth=data["birth"],
            address1=data["address1"],
            address2=data["address2"],
            phone=data["phone"],
            team_id=1,
        )
        return parent
    except Exception as e:
        print("190: ", e)
        return None


# GENERA TOKEN
@csrf_exempt
def signupView(request):
    # COMRPOBAR SI LOS DATOS SON LOS CORRECTOS
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
                {"Error": "Este correo electrónico ya está registrado."}
            )
        # Creamos el usuario en la base de datos User
        user = createUser(data)
        if data["rol"] == "trainer":
            trainer = createTrainer(data, user.id)
        # Autenticamos el usuario, para así añadir los datos restantes a la tabla entrenador
        if user is not None:
            # Creamos al entrenador
            if trainer:
                JWT = generateJWT(user)
                login(request, user)
                return JsonResponse(
                    {
                        "success": "El entrenador ha sido autenticado y creado.",
                        "JWT": JWT,
                    },
                    status=201,
                )
            return JsonResponse(
                {"El entrenador no ha sido autenticado ni creado"}, status=500
            )
        if data["rol"] == "parent":
            parent = createParent(user, user.id)
            if user is not None:
                if parent:
                    JWT = generateJWT(user)
                    login(request, user)
                    return JsonResponse(
                        {
                            "success": "El Padre ha sido autenticado y creado.",
                            "JWT": JWT,
                        },
                        status=201,
                    )
                return JsonResponse(
                    {"El entrenador no ha sido autenticado ni creado"}, status=500
                )


@csrf_exempt
def loginView(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = authenticate(request, username=data["email"], password=data["password"])
        if user is not None:
            # Iniciamos sesión
            login(request, user)
            # Generamos el token
            token = generateJWT(user)

            if token:
                print(token)
                return JsonResponse(
                    {
                        "success": "Usuario logeado y autenticado con éxito.",
                        "JWT": token,
                    },
                    status=200,
                )
            else:
                return JsonResponse({"error": "El token no se ha podido crear"})

        else:
            return JsonResponse({"error": "Email o contraseña incorrectas"})


@csrf_exempt
def logoutView(request):
    if request.method == "POST":
        # data = json.loads(request.body)
        logout(request)
        return JsonResponse({"success": "Sesión cerrada"})
