from django.db import models
from datetime import datetime
from members.models import *


class Message(models.Model):

    # Un entrenador puede escribir varias sesiones
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE,
        related_name="get_trainers_session",
        verbose_name="Trainer",
        default=1,
    )

    # Un jugador puede tener una o muchas sesiones
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="get_players_session",
        verbose_name="Players",
        default=1,
    )
    session_title = models.CharField(max_length=300, null=True, blank=True)
    session_description = models.CharField(max_length=300, null=True, blank=True)
    notification_title = models.CharField(max_length=300, null=True, blank=True)
    notification = models.CharField(max_length=300, null=True, blank=True)
    notice_title = models.CharField(max_length=300, null=True, blank=True)
    notice = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.player.parent.user.first_name + " " + self.trainer.user.first_name
