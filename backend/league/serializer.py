from rest_framework import serializers

# Los serializers permiten convertir objetos de Python, como
# modelos de Django en formatos de datos como JSON
from .models import Team


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
            'category',
            'league',
            'town',
        )
