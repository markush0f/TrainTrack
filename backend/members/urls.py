from . import views
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# DefaultRouter nos genera todas las vistas necesarias

# router = DefaultRouter()
# router.register("trainers", TrainerViewSet, basename="trainers")
# router.register("teams", TeamViewSet, basename="teams")
# # router.register('parents', ParentViewSet, basename='parents')

# # Definimos todas las rutas en urlpatterns
# urlpatterns = router.urls

urlpatterns = [
    path("", views.getRoutes),
    path("createtrainer", views.signup, name="create_trainer"),
    path("checkcodeteam", views.checkCodeTeam, name="check_code_team"),
    path("logintrainer", views.loginView, name="login_trainer"),
    path("authenticatejwt", views.verify_token, name="authenticate_jwt"),
    path("token", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
