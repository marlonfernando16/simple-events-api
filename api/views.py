
from rest_framework import viewsets, permissions

from . import models
from . import serializers
from api.validators import AppPermision, IsAdmin


class UserViewSet(viewsets.ModelViewSet):

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.AllowAny,)


class EventoViewSet(viewsets.ModelViewSet):

    queryset = models.Evento.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = serializers.EventoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EspecialidadeViewSet(viewsets.ModelViewSet):

    queryset = models.Especialidade.objects.all()
    serializer_class = serializers.EspecialidadeSerializer
    # permission_classes = [permissions.IsAuthenticated, IsAdmin]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class VagaViewSet(viewsets.ModelViewSet):

    queryset = models.Vaga.objects.all()
    serializer_class = serializers.VagaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CandidatoVagaViewSet(viewsets.ModelViewSet):

    queryset = models.CandidatoVaga.objects.all()
    serializer_class = serializers.CanddatoVagaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AvaliacaoEventoViewSet(viewsets.ModelViewSet):

    queryset = models.AvaliacaoEvento.objects.all()
    serializer_class = serializers.AvaliacaoEventoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
