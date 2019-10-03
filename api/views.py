from django.shortcuts import render

from rest_framework import viewsets, generics
from . import models
from . import serializers


class UserViewSet(viewsets.ModelViewSet):

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class EventoViewSet(viewsets.ModelViewSet):

    queryset = models.Evento.objects.all()
    serializer_class = serializers.EventoSerializer


class EspecialidadeViewSet(viewsets.ModelViewSet):

    queryset = models.Especialidade.objects.all()
    serializer_class = serializers.EspecialidadeSerializer


class VagaViewSet(viewsets.ModelViewSet):

    queryset = models.Vaga.objects.all()
    serializer_class = serializers.VagaSerializer


class CandidatoVagaViewSet(viewsets.ModelViewSet):

    queryset = models.CandidatoVaga.objects.all()
    serializer_class = serializers.CanddatoVagaSerializer


class AvaliacaoEventoViewSet(viewsets.ModelViewSet):

    queryset = models.AvaliacaoEvento.objects.all()
    serializer_class = serializers.AvaliacaoEventoSerializer
