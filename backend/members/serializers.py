from rest_framework import serializers

# Los serializers permiten convertir objetos de Python, como
# modelos de Django en formatos de datos como JSON
from .models import Trainer, Team


#  Esto son metadatos que se enviarán a nuestro Api REST de Trainer
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        read_only_fields = (
            "created_at",
            "updated_at",
        )
        fields = (
            "id",
            "name",
            "surname",
            "email",
            "birth",
            "password",
            "team",
        )


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        read_only_fields = (
            "created_at",
            "updated_at",
        )
        fields = (
            "id",
            "name",
        )
