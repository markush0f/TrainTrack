from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("members.urls")),
    path("api/league/", include("league.urls")),
    path("api/session/", include("session.urls")),
    path("api/forum/", include("forum.urls"))
]
# DO THE MIGRATIONS