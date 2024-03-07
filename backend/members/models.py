from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from localflavor.es.forms import ESIdentityCardNumberField
from league.models import Team
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# El BaseUserManager sirve para los admin

# Modelo de Entrenadores
class Trainer(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="get_teams",
        verbose_name="Team",
        default=1,
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Estos datos ya están en auth_user
    # email = models.EmailField(blank=False, null=False)
    # password = models.CharField(blank=False, null=True, max_length=255)
    # name = models.CharField(blank=False, null=False, max_length=255)
    # surname = models.CharField(blank=False, null=False, max_length=255)
    birth = models.DateField(blank=False, null=False)
    dni = ESIdentityCardNumberField(only_nif=True)
    address1 = models.CharField(blank=False, null=False, max_length=255)
    address2 = models.CharField(blank=False, null=True, max_length=255)
    phone = models.CharField(blank=False, null=False, max_length=255)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True)
    # a la contraseña ponerle un hash

    class Meta:
        verbose_name = "Trainer"
        verbose_name_plural = "Trainers"
        ordering = ["name"]

    def __str__(self):
        return self.name + " " + self.surname


# Modelo de los padres
class Parent(models.Model):
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE,
        related_name="get_trainers",
        verbose_name="Trainer",
        default=1,
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #  Estos datos ya están en auth_user
    # email = models.EmailField(blank=False, null=False)
    # password = models.CharField(blank=False, null=True, max_length=255)
    # name = models.CharField(blank=False, null=False, max_length=255)
    # surname = models.CharField(blank=False, null=False, max_length=255)
    birth = models.DateField(blank=False, null=False)
    dni = ESIdentityCardNumberField(only_nif=True)
    address1 = models.CharField(blank=False, null=False, max_length=255)
    address2 = models.CharField(blank=False, null=True, max_length=255)
    phone = models.CharField(blank=False, null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Parent"
        verbose_name_plural = "Parents"
        ordering = ["name"]

    def __str__(self):
        return self.name + " " + self.surname


# Modelo de Jugadores
class Player(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="get_team",
        verbose_name="Team",
        default=1,
    )
    parent = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE,
        related_name="get_parent",
        verbose_name="Parent",
        default=1,
    )
    name = models.CharField(blank=False, null=False, max_length=255)
    surname = models.CharField(blank=False, null=False, max_length=255)
    birth = models.DateField(blank=False, null=False)
    dni = ESIdentityCardNumberField(only_nif=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name + " " + self.surname


class formAccountParent(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class checkCodeTeam(models.Model):
    codeTeam = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
