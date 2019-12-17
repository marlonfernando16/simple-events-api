from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.User
        fields = ['nome', 'username', 'telefone', 'data_nascimento', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class EventoSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(many=False, read_only=True,
                                          slug_field='username')

    class Meta:
        model = models.Evento
        fields = ['id', 'nome', 'descricao', 'owner', 'data', 'local', 'finalizado', 'vagas']
        read_only_fields = ['owner', 'finalizado', 'vagas']

        depth = 1


class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Especialidade
        fields = '__all__'


class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vaga
        fields = '__all__'


class CanddatoVagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CandidatoVaga
        fields = '__all__'


class AvaliacaoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AvaliacaoEvento
        fields = '__all__'
