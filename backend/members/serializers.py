from rest_framework import serializers

# Los serializers permiten convertir objetos de Python, como
# modelos de Django en formatos de datos como JSON
from .models import Trainer, Parent
from django.contrib.auth.models import User


#  Esto son metadatos que se enviarán a nuestro Api REST de Trainer
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        read_only_fields = (
            "created_at",
            "updated_at",
        )
        fields = (
            "birth",
            "team",
        )


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = (
            "birth",
            "team",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
