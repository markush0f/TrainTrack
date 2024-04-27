from django.db import models
from members.models import Parent, Trainer
from league.models import Team
from django.contrib.auth.models import User


class Forum(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # parent = models.OneToOneField(Parent, on_delete=models.CASCADE,)
    # trainer = models.OneToOneField(Trainer, on_delete=models.CASCADE)
    # title = models.CharField(max_length=300, null=300, blank=True)
    title = models.CharField(max_length=300, null=300, blank=True)
    message = models.CharField(max_length=300, null=300, blank=True)
    author = models.CharField(max_length=300, null=300, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    