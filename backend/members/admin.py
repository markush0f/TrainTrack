from django.contrib import admin

# Register your models here.
from .models import Trainer, Player, Team

admin.site.register(Team)
admin.site.register(Trainer)
admin.site.register(Player)

# https://www.youtube.com/watch?v=WMR4qdYFW-8&t=921s
