from django.db import models

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
    train_session_tittle = models.CharField(max_length=300)
    train_description = models.CharField(max_length=300)
    train_created_at = models.CharField(max_length=300)
    notification_tittle = models.CharField(max_length=300)
    notification = models.CharField(max_length=300)
    notification_created_at = models.CharField(max_length=300)

    def __str__(self):
        return self.name + " " + self.surname
