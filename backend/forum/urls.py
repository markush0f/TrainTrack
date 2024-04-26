from . import views
from django.urls import path, include

urlpatterns = [
    path("loadmessages", views.loadMessages, name="load_messages"),
    path("sendmessage", views.sendMessage, name="send_message"),
]
