from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
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


def getRoutes(request):
    routes = ["/api/token", "/api/token/refresh", "/api/trainers", "/api/parents"]
    return JsonResponse(routes, safe=False)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token["email"] = user.email

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


# class ParentViewSet(viewsets.ModelViewSet):
#     queryset = Team.objects.all()
#     serializer_class = ParentSerializer

# Validamos el token JWT
@permission_classes([IsAuthenticated])
def verify_token(request):
    # Si la solicitud ha llegado hasta aquí, significa que el token JWT ha sido verificado con éxito
    return JsonResponse({"valid": True})


# Generamos el token JWT
def generateJWT(user):
    tokens = RefreshToken.for_user(user)
    access_token = str(tokens.access_token)
    # refresh_token = str(refresh)
    return access_token


# Validamos el token JWT
# Requerimos autenticación a la función
# @permission_classes([IsAuthenticated])
# def authenticateJWT(request):
#     data = request.headers
#     # print(data["Authorization"])
#     authorizationHeader = data["Authorization"]
#     if authorizationHeader and authorizationHeader.startswith("Bearer "):
#         print("Aqui si")
#         tokenJWT = authorizationHeader.split(" ")[1]
#         try:
#             # Decodificamos el token JWT
#             payload = jwt.decode(tokenJWT, settings.SECRET_KEY, algorithms=["HS256"])
#             user = User.objects.get(pk=payload.get("user_id"))
#             request.user = user
#             return None
#             # Se sigue ejecutando la función
#         except jwt.ExpiredSignatureError:
#             return JsonResponse(
#                 {"error": "Token expirado, debe iniciar sesión"}, status=401
#             )
#     else:
#         return JsonResponse({"error": "Token no enviado"}, status=401)


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


@csrf_exempt
def loginView(request):
    if request.method == "POST":
        data = json.loads(request.body)
        # CSRF = data["csrf"]
        # if not CSRF:
        #     return JsonResponse({"error": "Token CSRF no válido"}, status=403)
        # Autenticamos el usuario
        user = authenticate(request, username=data["email"], password=data["password"])
        if user is not None:
            # Iniciamos sesión
            login(request, user)
            # Generamos el token
            token = generateJWT(user)
            return JsonResponse(
                {"success": "Usuario logeado y autenticado con éxito.", "token": token},
                status=200,
            )
        else:
            return JsonResponse({"error": "Email o contraseña incorrectas"})
