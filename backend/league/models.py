from datetime import timezone
from django.db import models
import uuid

# Modelo de equipos
class Team(models.Model):
    team_code = models.UUIDField(default=uuid.uuid4, editable=False,unique=True)
    name = models.CharField(blank=False, null=False, max_length=255)
    category = models.CharField(blank=False, null=False, max_length=255)
    league = models.CharField(blank=False, null=False, max_length=255)
    town = models.CharField(blank=False, null=False, max_length=255)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        ordering = ["name"]
        # mas campos

    def __str__(self):
        return self.name
