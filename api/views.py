from django.shortcuts import render

from rest_framework import generics
from . import models
from . import serializers


class UserList(generics.ListCreateAPIView):

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class EventoList(generics.ListCreateAPIView):

    queryset = models.Evento.objects.all()
    serializer_class = serializers.EventoSerializer


class EspecialidadeList(generics.ListCreateAPIView):

    queryset = models.Especialidade.objects.all()
    serializer_class = serializers.EspecialidadeSerializer


class VagaList(generics.ListCreateAPIView):

    queryset = models.Vaga.objects.all()
    serializer_class = serializers.VagaSerializer


class CandidatoVagaList(generics.ListCreateAPIView):

    queryset = models.CandidatoVaga.objects.all()
    serializer_class = serializers.CanddatoVagaSerializer


class AvaliacaoEventoList(generics.ListCreateAPIView):

    queryset = models.AvaliacaoEvento.objects.all()
    serializer_class = serializers.AvaliacaoEventoSerializer
