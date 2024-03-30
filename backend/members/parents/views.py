import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from league.models import Team
from members.utils import decodeJWT, generateJWT
from members.models import Parent, Trainer
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def createParent(data, user_id):
    try:
        parent = Parent.objects.create(
            user_id=user_id,
            birth=data.get("birth"),
            address1=data.get("address1"),
            address2=data.get("address2"),
            phone=data.get("phone"),
            verify=0,
        )
        return parent
    except Exception as e:
        print("190: ", e)
        return None


@csrf_exempt
def signupViewParent(request):
    from members.views import createUser

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("Data:", data)

            errors = {}
            # Comprobamos si hay campos vacíos
            for key, value in data.items():
                if not value:
                    errors[f"{key}Empty"] = f"El campo {key} no puede estar vacío"
                    print(f"Key: {key}, Value: {value}")
            if errors:
                return JsonResponse({"Errors": errors})

            # Verificar si el correo electrónico ya está registrado
            if "email" in data:
                if User.objects.filter(email=data["email"]).exists():
                    return JsonResponse(
                        {"Error": "Este correo electrónico ya está registrado."}
                    )

            # Verificar si el equipo existe y la contraseña del equipo es correcta
            teamCode = data["teamCode"]
            teamPassword = data["teamPassword"]
            team = Team.objects.filter(team_code=teamCode).first()
            if not team or team.team_password != teamPassword:
                return JsonResponse(
                    {
                        "error": "No se encuentra ningún equipo con este código o la contraseña es incorrecta."
                    }
                )

            # Crear el usuario y el padre
            user = createUser(data)
            if user is not None:
                parent = createParent(data, user.id)
                if parent:
                    return JsonResponse(
                        {
                            "success": "Debe esperar a que el entrenador confirme su registro, en cuanto confirme le llegará un correo electrónico."
                        }
                    )

        except json.JSONDecodeError:
            return JsonResponse(
                {"error": "JSON inválido proporcionado en el cuerpo de la solicitud."}
            )
        except Exception as e:
            return JsonResponse({"error": f"{str(e)}"})

    return JsonResponse({"error": "Se requiere un método POST válido."})




# Recogemos los padres segúun al entrenador al que pertenecen
def parentsByTrainer(request):
    if request.method == "GET":
        payload = decodeJWT(request)
        try:
            if payload["rol"] == "trainer":
                parentsList = []
                trainer = Trainer.objects.get(user_id=payload["user_id"])
                parents = Parent.objects.filter(trainer_id=trainer.id)
                for parent in parents:
                    parentsList.append(
                        {
                            "name": parent.user.first_name,
                            "username": parent.user.last_name,
                            "id": parent.id,
                        }
                    )
                return JsonResponse({"parents": parentsList})
        except Exception as e:
            return JsonResponse(
                {"error": "Se produjo un error al procesar la solicitud"}
            )


def profileParent(request, payload):
    payload = decodeJWT(request)
    try:
        user = User.objects.get(id=payload["user_id"])
        parent = Parent.objects.get(user_id=payload["user_id"])
        team = Team.objects.get(id=parent.trainer.team)
        profile = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "address1": parent.address1,
            "address2": parent.address2,
            "team": (team.name if team else "Sin equipo"),
        }
        return JsonResponse({"profile": profile}, safe=False)
    except User.DoesNotExist:
        return JsonResponse("Usuario no encontrado", status=404)
    except parent.DoesNotExist:
        return JsonResponse("Padre no encontrado", status=404)
    except Team.DoesNotExist:
        return JsonResponse("Equipo no encontrado", status=404)

