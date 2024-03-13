from rest_framework import serializers
from models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        read_only_fields = (
            "created_at",
            "updated_at",
        )
        fields = "__all__"
