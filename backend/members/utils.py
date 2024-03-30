from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
from .serializers import *
import json, re, jwt
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Verificamos el token
@csrf_exempt
def verifyToken(request):
    if request.method == "POST":
        token = request.headers["Authorization"]
        # return JsonResponse({"error": token})
        # print(request.headers["Authorization"])
        if token and token.startswith("Bearer "):
            print("token recogido y empieza por Bearer")
            print(token)

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


# PRIMERO SE DEBE REGISTAR EL USUARIO, LUEGO EL USUARIO INTRODUCIRÁ EL CODIGO Y CONTRASEÑA DEL EQUIPO, A RAIZ DE ESO
# AL ENTRENADOR SEGÚN EL EQUIPO LE LLEGARÁ UNA PETICION PARA ACEPTAR AL PADRE
# POR LO QUE EL USUARIO ACCEDERÁ A LAS RUTAS SIGUIENDO LOS SIGUIENTES REQUISITOS:
# CHECKCODETEAM: SE NECESITA QUE EL USUARIO SE HAYA REGISTRADO, GUARDAREMOS EN EL TOKEN EL ID
# LOGIN: SE NECESITA QUE EL USUARIO HAYA SIDO VERIFICADO POR EL ENTRENADOR

# TOKEN:
# user_id
# CUANDO EL USUARIO SE REGISTRE PERO NO HAYA REGISTRADO EL EQUIPO, NO PODRÁ INICIAR SESIÓN, ESTO LO HAREMOS:
# ENVIAREMOS EN EL TOKEN EL USER_ID, Y COMPROBAMOS SI EL VERIFY ES TRUE O FALSE


# Comprobamos si en e token JWT está el
# Generamos el token JWT
def generateJWT(user, rol=None):
    print("Creando token")
    if not user:
        print("Usuario no enviado")
        return None
    payload = {"user_id": user.id}
    if rol and rol in ["trainer", "parent"]:
        payload["rol"] = rol

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token


# Decodificamos el JWT
def decodeJWT(request):
    try:
        token = request.headers.get("Authorization")
        if token and token.startswith("Bearer "):
            print("Token recogido y empieza por Bearer")
            tokenJWT = token.split(" ")[1]
            # Decodificamos el token JWT
            payload = jwt.decode(tokenJWT, settings.SECRET_KEY, algorithms=["HS256"])
            return payload
        else:
            print("Token de autorización no encontrado o formato incorrecto")
            return None
    except jwt.ExpiredSignatureError:
        print("Token JWT expirado")
        return None
    except jwt.InvalidTokenError as e:
        print("Token JWT inválido:", e)
        return None
    except Exception as e:
        print("Error desconocido al decodificar el token JWT:", e)
        return None


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
