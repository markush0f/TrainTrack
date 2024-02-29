from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# viewsets es una clase que combina las funciones de varias
# vistas genéricas para proporcionar un conjunto
# completo de operaciones CRUD para un modelo especifico

from .models import *
from .serializers import *


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

    # Filtramos por equipo:
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


# # CRUD de Trainers
# # Vista que obtiene todos los entrenadores
# class TrainerList(generics.ListCreateAPIView):
#   queryset = Trainer.objects.all()
#   serializer_class = TrainerSerializer
# # Vista que nos permite Añadir, actualizar y eliminar un entrenador
# class TrainerDetail(generics.RetrieveUpdateDestroyAPIView):
#   queryset = Trainer.objects.all()
#   serializer_class = TrainerSerializer

# # CRUD de Teams

# class TeamList(generics.ListCreateAPIView):
#   queryset = Team.objects.all()
#   serializer_class = TrainerSerializer
# class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
#   queryset = Team.objects.all()
#   serializer_class = TeamSerializer
