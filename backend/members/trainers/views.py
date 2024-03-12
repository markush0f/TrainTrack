from django.http import JsonResponse
from backend.league.models import Team
from members.utils import generateJWT, verifyToken
from members.models import Parent, Trainer
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def singupTrainerre(request, user):
    JWT = generateJWT(user)
    if JWT:
        login(request, user)
        return JsonResponse(
            {
                "success": "El entrenador ha sido autenticado y creado.",
                "JWT": JWT,
            },
            status=201,
        )
    return JsonResponse({"El entrenador no ha sido autenticado ni creado"}, status=500)


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


def profileTrainer(request):
    payload = verifyToken(request, True)
    try:
        user = User.objects.get(id=payload["user_id"])
        trainer = Trainer.objects.get(user_id=payload["user_id"])
        team = Team.objects.get(id=trainer.team_id)
        profile = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "address1": trainer.address1,
            "address2": trainer.address2,
            "team": (team.name if team else "Sin equipo"),
        }
        return JsonResponse({"profile": profile}, safe=False)
    except User.DoesNotExist:
        return JsonResponse("Usuario no encontrado", status=404)
    except Trainer.DoesNotExist:
        return JsonResponse("Entrenador no encontrado", status=404)
    except Team.DoesNotExist:
        return JsonResponse("Equipo no encontrado", status=404)
