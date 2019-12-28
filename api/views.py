from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from api import models, serializers, validators


class UserViewSet(viewsets.ModelViewSet):

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.AllowAny,)


class EventoViewSet(viewsets.ModelViewSet):

    queryset = models.Evento.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = serializers.EventoSerializer

    def perform_create(self, serializer):
        evento = serializer.save(owner=self.request.user)
        for vaga in self.request.data.get('vagas'):
            print(vaga[0])
            print(vaga[1])
            especialidade = get_object_or_404(models.Especialidade, nome=vaga[0])
            print(especialidade)
            models.Vaga.objects.create(
                evento=evento,
                qtd_vagas=vaga[1],
                especialidade=especialidade
            )


class EspecialidadeViewSet(viewsets.ModelViewSet):

    queryset = models.Especialidade.objects.all()
    serializer_class = serializers.EspecialidadeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class VagaViewSet(viewsets.ModelViewSet):

    queryset = models.Vaga.objects.all()
    serializer_class = serializers.VagaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CandidatoVagaViewSet(viewsets.ModelViewSet):

    queryset = models.CandidatoVaga.objects.all()
    serializer_class = serializers.CandidatoVagaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AvaliacaoEventoViewSet(viewsets.ModelViewSet):

    queryset = models.AvaliacaoEvento.objects.all()
    serializer_class = serializers.AvaliacaoEventoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def candidatar(request, id):
    vaga = get_object_or_404(models.Vaga, pk=id)
    if request.user.username == vaga.evento.owner.username:
        return Response(
            data={"detail": "Peladeiro não encontrado."},
            status=status.HTTP_304_NOT_MODIFIED
        )
    cv = models.CandidatoVaga.objects.create(candidato=request.user, vaga=vaga, state_vaga=3)
    print(cv)
    serializer = serializers.CandidatoVagaSerializer(cv)
    print(serializer)
    return Response(
        data=serializer.data,
        status=status.HTTP_200_OK
    )
