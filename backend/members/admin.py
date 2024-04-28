from django.contrib import admin

# Register your models here.
from .models import Trainer, Player, Parent

admin.site.register(Trainer)
admin.site.register(Player)
admin.site.register(Parent)
