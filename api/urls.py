from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('eventos', views.EventoViewSet)
router.register('especialidades', views.EspecialidadeViewSet)
router.register('candidatosvaga', views.CandidatoVagaViewSet)
router.register('vagas', views.VagaViewSet)
router.register('avaliacoes-evento', views.AvaliacaoEventoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
