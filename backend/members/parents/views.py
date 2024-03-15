from django.http import JsonResponse
from league.models import Team
from members.utils import generateJWT, verifyToken, decodeJWT
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
            team_id=1,
        )
        return JsonResponse(
            {
                "success": True,
                "parent": parent,
            },
            safe=False,
        )
    except Exception as e:
        print("190: ", e)
        return None


def signupParent(request, user):
    JWT = generateJWT(user, "parent")
    if JWT:
        login(request, user)
        return JsonResponse(
            {
                "success": "El Padre ha sido autenticado y creado.",
                "JWT": JWT,
            },
            status=201,
        )
    return JsonResponse({"El entrenador no ha sido autenticado ni creado"}, status=500)


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
    # payload = decodeJWT(request)

    try:
        user = User.objects.get(id=payload["user_id"])
        parent = Parent.objects.get(user_id=payload["user_id"])
        team = Team.objects.get(id=parent.team_id)
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
