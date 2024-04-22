from django.db import models
from datetime import datetime
from members.models import *


class Events(models.Model):

    # Un entrenador puede escribir varias sesiones
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE,
        related_name="get_trainers_session",
        verbose_name="Trainer",
        null=True,
    )

    # Un jugador puede tener una o muchas sesiones
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="get_players_session",
        verbose_name="Players",
        null=True,
    )
    title = models.CharField(max_length=300, null=300, blank=True)
    # Sesión de entrenador a padre
    session_description = models.CharField(max_length=300, null=True, blank=True)
    # Notificación de padre a entrenador
    notification = models.CharField(max_length=300, null=True, blank=True)
    # Aviso de entrenador a padre
    notice = models.CharField(max_length=300, null=True, blank=True)
    other = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class Calendar(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="get_team_foro",
        verbose_name="Team",
        null=True,
    )
    title_event = models.CharField(max_length=300, null=False, blank=False)
    description_event = models.CharField(max_length=300, null=True, blank=True)
    event_date = models.DateField()
    event_time = models.CharField(max_length=300, null=False, blank=False)
    color_event = models.CharField(max_length=300, null=False, blank=False)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title_event
