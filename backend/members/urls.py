from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

# DefaultRouter nos genera todas las vistas necesarias

router = DefaultRouter()
router.register('trainers', TrainerViewSet, basename='trainers')
router.register('teams', TeamViewSet, basename='teams')

# Definimos todas las rutas en urlpatterns
urlpatterns = router.urls

urlpatterns += [
  path('createuser', signup, name="create_parent"),
  path('checkcodeteam', checkCodeTeam, name="check_code_team"),
]

