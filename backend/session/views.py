from rest_framework import viewsets
from models import Message

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = Message
