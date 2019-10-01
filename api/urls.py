
from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^eventos/$', views.EventoList.as_view(), name='evento-list'),
    url(r'^especialidades/$', views.EspecialidadeList.as_view(), name='especialidade-list'),
    url(r'^candidatosvaga/$', views.CandidatoVagaList.as_view(), name='candidatovaga-list'),
    url(r'^vagas/$', views.VagaList.as_view(), name='vaga-list'),
    url(r'^avaliacoes-evento/$', views.AvaliacaoEventoList.as_view(), name='avaliacaoevento-list'),
]
