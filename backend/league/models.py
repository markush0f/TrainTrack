from datetime import timezone
from django.db import models
import uuid


# Modelo de equipos
class Team(models.Model):
    team_code = models.CharField(blank=False, null=False, max_length=255)
    name = models.CharField(blank=False, null=False, max_length=255)
    category = models.CharField(blank=False, null=False, max_length=255)
    league = models.CharField(blank=False, null=False, max_length=255)
    town = models.CharField(blank=False, null=False, max_length=255)
    team_password = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        ordering = ["name"]
        # mas campos

    def __str__(self):
        return self.name + "-" + self.category


class Shields(models.Model):
    route = models.CharField(max_length=255)
    team = models.OneToOneField(
        Team,
        on_delete=models.CASCADE,
        related_name="get_team_shield",
        verbose_name="Team",
        default=1,
    )
