from django.db import models
from league.models import Team
from django.contrib.auth.models import User


class Forum(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=300, null=300, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.user + self.message