from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
from .serializers import *
import json, re, jwt
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def verifyToken(request):
    if request.method == "POST":
        token = request.headers["Authorization"]
        # return JsonResponse({"error": token})
        # print(request.headers["Authorization"])
        if token and token.startswith("Bearer "):
            print("token recogido y empieza por Bearer")
            print(token)
            # SEGÚN EL ID, ENVIAR EL ROL DE SI ES PADRE O ENTRENADOR
            try:
                tokenJWT = token.split(" ")[1]
                # Decodificamos el token JWT
                payload = jwt.decode(
                    tokenJWT, settings.SECRET_KEY, algorithms=["HS256"]
                )
                print(payload)
                print("Payload:", payload)
                return JsonResponse(
                    {
                        "message": "Token válido",
                        "valid": True,
                        "rol": payload["rol"],
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
def generateJWT(user, rol):
    payload = {"user_id": user.id}
    if rol:
        payload["rol"] = rol
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token


# Decodificamos el JWT
def decodeJWT(request):
    token = request.headers["Authorization"]
    if token and token.startswith("Bearer "):
        print("Token recogido y empieza por Bearer")
        print(token)
        try:
            tokenJWT = token.split(" ")[1]
            # Decodificamos el token JWT
            payload = jwt.decode(tokenJWT, settings.SECRET_KEY, algorithms=["HS256"])
            return payload
        except Exception as e:
            print("Error: ", e)


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
