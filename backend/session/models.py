from django.db import models

from members.models import *

# Create your models here.


class trainingSessions(models.Model):
  
  # Un entrenador puede escribir varias sesiones
    trainer_id = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE,
        related_name="get_trainers",
        verbose_name="Trainer",
        default=1,
    )
    
    # Un jugador puede tener una o muchas sesiones
    player_id = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="get_players",
        verbose_name="Players",
        default=1,
    )
    
    train_description = models.CharField(max_length=300)
