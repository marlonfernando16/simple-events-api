
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from . import models
from . import serializers
from api.validators import AppPermision, IsAdmin


class UserViewSet(viewsets.ModelViewSet):

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventoViewSet(viewsets.ModelViewSet):

    queryset = models.Evento.objects.all()
    permission_classes = [AppPermision]

    serializer_class = serializers.EventoSerializer
    # permission_classes = [AppPermision]


class EspecialidadeViewSet(viewsets.ModelViewSet):

    queryset = models.Especialidade.objects.all()
    serializer_class = serializers.EspecialidadeSerializer
    # permission_classes = [permissions.IsAuthenticated, IsAdmin]


class VagaViewSet(viewsets.ModelViewSet):

    queryset = models.Vaga.objects.all()
    serializer_class = serializers.VagaSerializer
    # permission_classes = [AppPermision]


class CandidatoVagaViewSet(viewsets.ModelViewSet):

    queryset = models.CandidatoVaga.objects.all()
    serializer_class = serializers.CanddatoVagaSerializer
    # permission_classes = [AppPermision]


class AvaliacaoEventoViewSet(viewsets.ModelViewSet):

    queryset = models.AvaliacaoEvento.objects.all()
    serializer_class = serializers.AvaliacaoEventoSerializer
    # permission_classes = [AppPermision]
