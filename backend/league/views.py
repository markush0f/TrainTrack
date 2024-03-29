from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
import json
from .serializer import TeamSerializer
from .models import Team, Shields


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


def listTeams(request):
    # return JsonResponse({"request":category}, safe=False)
    if request.method == "GET":
        category = request.GET.get("category")
        if category:
            try:
                teamByCategory = Team.objects.filter(category=category)
                teams = []
                for team in teamByCategory:
                    teamData = {
                        "name": team.name,
                        "matchPlayed": 0,
                        "matchWinned": 0,
                        "matchDrawed": 0,
                        "matchLosed": 0,
                        "points": 0,
                    }
                    teams.append(teamData)
                return JsonResponse({"team": teams})
            except Team.DoesNotExist:
                return JsonResponse("No existe el equipo", safe=False)


def listShields(request):
    if request.method == "GET":
        shields = Shields.objects.all()
        imgs = [shield.route for shield in shields]
        return JsonResponse({"imgs": imgs})
    