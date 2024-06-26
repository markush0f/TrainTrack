# Recogemos los jugadores según el equipo
import json
from django.http import JsonResponse
from members.utils import *
from members.models import Trainer, Player, Team
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


def playersByTeams(request):
    if request.method == "GET":
        payload = decodeJWT(request)
        try:
            if payload["rol"] == "trainer":
                user = User.objects.get(id=payload["user_id"])
                trainer = Trainer.objects.get(user_id=user.id)
                players = Player.objects.filter(team=trainer.team)
                playerList = []
                if players.exists():
                    for player in players:
                        # Aquí agregamos cada jugador a la lista, en lugar de sobrescribir la lista en cada iteración
                        playerList.append(
                            {
                                "id": player.id,
                                "name": player.name,
                                "surname": player.surname,
                                "parent": player.parent.user.first_name,
                                "position": "Delantero",
                                "goals": 34,
                                "address1": player.parent.address1,
                                "address2": player.parent.address2,
                            }
                        )
                    # Luego retornamos la lista completa de jugadores
                    return JsonResponse({"players": playerList})
                else:
                    return JsonResponse({"error": "No existen jugadores en ese equipo"})
            else:
                return JsonResponse({"error": "No existen jugadores en ese equipo"})

        except Trainer.DoesNotExist:
            return JsonResponse(
                {"error": "No se encontró ningún entrenador con el ID proporcionado"}
            )
        except Player.DoesNotExist:
            return JsonResponse({"error": "No existen jugadores en ese equipo"})

        except Exception as e:
            return JsonResponse(
                {"error": "Se produjo un error al procesar la solicitud"}
            )


# Recogemos los jguadores según la categoría


def playersByCategory(request):
    if request.method == "GET":
        category = request.GET.get("category")
        if category:
            teams = Team.objects.filter(category=category)
            playersList = []
            for team in teams:
                players_in_team = Player.objects.filter(team_id=team.id)
                for player in players_in_team:
                    playersList.append(
                        {
                            "name": player.name,
                            "surname": player.surname,
                            "goals": 0,
                            "assistance": 0,
                            "games_played": 0,
                        }
                    )
            return JsonResponse({"players": playersList})
        else:
            return JsonResponse({"error": "Categoría no encontrada"}, status=400)
    else:
        return JsonResponse({"error": "Método no válido"}, status=405)


@csrf_exempt
def players(request):
    # Creamos un jugador
    if request.method == "POST":
        data = json.loads(request.body)
        payload = decodeJWT(request)
        try:
            trainer = Trainer.objects.get(user_id=payload["user_id"])
            player = Player.objects.create(
                name=data["name"],
                surname=data["surname"],
                birth=data["birth"],
                team_id=trainer.team_id,
                parent_id=data["parent_id"],
            )
            return JsonResponse({"success": True})
        except Trainer.DoesNotExist:
            return JsonResponse(
                {"error": "No se encontró ningún entrenador con el ID proporcionado"},
                status=404,
            )
        except Exception as e:
            return JsonResponse(
                {"error": "Se produjo un error al procesar la solicitud"}, status=500
            )
    else:
        return JsonResponse(
            {"error": "No tienes permisos para agregar jugadores"}, status=403
        )


# Muestra la información de un jugador
def profilePlayers(request):
    if request.method == "GET":
        data = json.loads(request.body)
        payload = decodeJWT(request)
        if payload:
            try:
                if data["player_id"]:
                    player = Player.objects.get(id=data["player_id"])
                    dataPlayer = {
                        "name": player.name,
                        "surname": player.surname,
                        "birth": player.birth,
                    }
            except Exception as e:
                return JsonResponse(
                    {"error": "Se produjo un error al procesar la solicitud"},
                    status=500,
                )


# models.ImageField
@csrf_exempt
def removePlayer(request):
    
    if request.method == "POST":
        payload = decodeJWT(request)
        if payload["rol"] == "trainer":
            try:
                data = json.loads(request.body)
                player_id = data.get("id")
                player = Player.objects.get(id=player_id)
                playerRemoved = {
                    "id": player.id,
                    "nombre": player.name,
                    "apellido": player.surname,
                }
                player.delete()
                return JsonResponse(
                    {"success": True, "jugador_eliminado": playerRemoved}
                )
            except Player.DoesNotExist:
                return JsonResponse({"error": "El jugador no existe"})
            except Exception as e:
                return JsonResponse(
                    {"error": str(e)}
                )
    else:
        return JsonResponse({'error': 'Metodo no valido'})