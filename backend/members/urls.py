from members.players.views import playersByCategory, players, playersByTeams
from . import views
from django.urls import path, include
from .views import *
from .parents.views import parentsByTrainer
from .utils import *
from rest_framework.routers import DefaultRouter


# DefaultRouter nos genera todas las vistas necesarias
router = DefaultRouter()
router.register("trainers", TrainerViewSet, basename="trainers")
router.register("parents", ParentViewSet, basename="parents")
router.register("users", UserViewSet)
# # Definimos todas las rutas en urlpatterns
# urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
    path("signup", views.signupView, name="signup"),
    path("checkcodeteam", views.checkCodeTeam, name="check_code_team"),
    path("login", views.loginView, name="login"),
    path("logout", views.logoutView, name="logout"),
    path("authenticatejwt", views.verifyToken, name="authenticate_jwt"),
    path("profile", views.profile, name="profile"),
    path("players", players, name="parents_by_parent"),
    path("playersbyteam", playersByTeams, name="players_by_team"),
    path("parents/bytrainer", parentsByTrainer, name="parents_by_parent"),
    path("players/bycategory", playersByCategory, name="players_by_category"),
]
