from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Crear un administrador
# Modelo de Equipos
# Los equipos ponerlos en una app distinta, cuyo nombre será algo relacionado con una liga
class Team(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        ordering = ["name"]
        # mas campos

    def __str__(self):
        return self.name


# Modelo de Entrenadores
class Trainer(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    surname = models.CharField(blank=False, null=False, max_length=255)
    email = models.EmailField(blank=False, null=False)
    birth = models.DateField(blank=False, null=False)
    password = models.CharField(blank=False, null=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="get_teams",
        verbose_name="Team",
        default=1 
    )
    # a la contraseña ponerle un hash
    # añadir address y country
    # Añadir mas maneras de contactos

    # team_id haremos una clave foranea con la de la base de datos de team

    class Meta:
        verbose_name = "Trainer"
        verbose_name_plural = "Trainers"
        ordering = ["name"]

    def __str__(self):
        return self.name


# Modelo de Jugadores
class Player(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    email = models.EmailField(blank=False, null=False)
    birth = models.DateField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # categoria del jugador
    # team_id haremos una clave foranea con la de la base de datos de team
    # Añadir mas maneras de contactos
