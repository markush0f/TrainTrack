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
    # Evento global para todos los padres.
    event = models.CharField(max_length=300, null=True, blank=True)
    # dia que se producirá el evento
    day_event = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.player.parent.user.first_name + " " + self.trainer.user.first_name
