from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import logout
from members.trainers.views import profileTrainer
from members.parents.views import profileParent
from .models import *
from .serializers import *
from django.contrib.auth import authenticate, login
import json
from .utils import *


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


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = ParentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@csrf_exempt
def checkCodeTeam(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print("Data: ", data)
        payload = decodeJWT(request)
        if payload["user_id"]:
            print("Codigo recibido desde el token")
            if data["codeTeam"] and data["password"]:
                try:
                    codeTeam = Team.objects.all().filter(team_code=data["codeTeam"])
                    password = Team.objects.all().filter(team_password=data["password"])
                    if password and codeTeam:
                        # PONER LA VALIDACION CORRECTA
                        return JsonResponse({"success": "Datos correctos"})
                    else:
                        return JsonResponse(
                            {"error": "Contraseña o codigo de equipo incorrecto."}
                        )
                except Exception as e:
                    return JsonResponse({"error": e})
        else:
            return JsonResponse({"error": "Debe registrarse primero"})


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
        return JsonResponse({"error": e})


@csrf_exempt
def loginView(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user = authenticate(
                request,
                username=data.get("email", ""),
                password=data.get("password", ""),
            )

            if user is None:
                return JsonResponse(
                    {"error": "Correo electrónico o contraseña incorrectos"}
                )

            parent = Parent.objects.filter(user_id=user.id).first()
            trainer = Trainer.objects.filter(user_id=user.id).first()

            if parent:
                if parent.verify != 0:
                    login(request, user)
                    rol = "parent"
                    token = generateJWT(user, rol)
                    if token:
                        return JsonResponse(
                            {"success": True, "token": token, "rol": rol}
                        )
                else:
                    return JsonResponse({"denied": "Su cuenta no está verificada."})

            elif trainer:
                login(request, user)
                rol = "trainer"
                token = generateJWT(user, rol)
                if token:
                    return JsonResponse({"success": True, "token": token, "rol": rol})

            else:
                return JsonResponse(
                    {"error": "No se encontró el perfil asociado al usuario."}
                )

        except json.JSONDecodeError:
            return JsonResponse(
                {"error": "JSON inválido proporcionado en el cuerpo de la solicitud."}
            )

        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Se requiere un método POST válido."})


# Enviaremos los padres que no estan verificados
def getUnverifiedParents(request):
    if request.method == "GET":
        try:
            payload = decodeJWT(request)
            user_id = payload.get("user_id")

            if user_id:
                unverifiedParents = Parent.objects.filter(verify=0)
                # return JsonResponse({"error":unverifiedParents})
                print(unverifiedParents)
                if unverifiedParents:
                    print("si existe")
                    parentsData = [
                        {
                            "id": parent.id,
                            "name": parent.user.first_name,
                            "surname": parent.user.last_name,
                            "DNI": parent.dni,
                        }
                        for parent in unverifiedParents
                    ]
                    return JsonResponse({"unverified": True, "parents": parentsData})
                else:
                    return JsonResponse(
                        {
                            "unverified": False,
                            "message": "No hay padres no verificados para este usuario.",
                        }
                    )
            else:
                return JsonResponse(
                    {"error": "Token JWT inválido o ausente."}, status=400
                )

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Método no válido."}, status=405)


@csrf_exempt
def manageRequestParent(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            decision = data.get("decision")
            parentId = data.get("parentId")
            # return JsonResponse({"error": data})
            if decision is not None and parentId is not None:
                parent = Parent.objects.filter(id=parentId).first()

                if parent:
                    if decision:
                        print("Decisión aprobada")
                        parent.verify = True
                        parent.save()
                        # Aquí puedes enviar un correo electrónico al padre
                        return JsonResponse(
                            {
                                "accepted": "Padre aceptado correctamente",
                                "success": True,
                            }
                        )
                    else:
                        print("Decisión denegada")
                        # user = User.objects.filter(id=parent.user).first()
                        user = parent.user
                        parent.delete()
                        user.delete()
                        # Aquí puedes enviar un correo electrónico al padre
                        return JsonResponse(
                            {
                                "denied": "Padre no aceptado y eliminado correctamente",
                                "success": True,
                            }
                        )

                else:
                    return JsonResponse(
                        {"error": f"No se encontró el padre con el ID recibido"},
                        status=400,
                    )
            else:
                return JsonResponse({"error": "Faltan parámetros"}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def logoutView(request):
    if request.method == "POST":

        # data = json.loads(request.body)
        logout(request)
        # Eliminar el token
        return JsonResponse({"success": "Sesión cerrada", "destroy": True})
    return JsonResponse({"error": "No se pudo cerrar la sesión"})


def profile(request):
    if request.method == "GET":
        payload = decodeJWT(request)
        print(payload["rol"])
        try:
            if payload["rol"] == "trainer":
                return profileTrainer(request, payload)
            if payload["rol"] == "parent":
                return profileParent(request, payload)
        except Exception as e:
            return JsonResponse({"error": str(e)})
