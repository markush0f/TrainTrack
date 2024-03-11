from django.shortcuts import render
from rest_framework import viewsets

from .serializer import TeamSerializer
from .models import Team

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    
