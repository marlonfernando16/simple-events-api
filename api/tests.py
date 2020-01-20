from django.test import TestCase
from api import models
from model_mommy import mommy
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token


class UserTestCase(TestCase):
    def setUp(self):

        self.usuario_candidato = mommy.make(
            models.User,
            username='userteste1',
            nome='userteste1',
            telefone=99999999,
            email='userteste.com',
            data_nascimento="1998-08-03"
        )
        self.usuario_candidato.set_password('123')
        self.usuario_candidato.save()

        self.usuario_admin = mommy.make(
            models.User,
            username='admin',
            nome='admin',
            telefone=99999999,
            email='admin.com',
            data_nascimento="1998-08-03",
            admin=True
        )
        self.usuario_admin.set_password('123')
        self.usuario_admin.save()

        (token, created) = Token.objects.get_or_create(user=self.usuario_candidato)
        self.client_candidato = APIClient()
        self.client_candidato.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        (token, created) = Token.objects.get_or_create(user=self.usuario_admin)
        self.client_admin = APIClient()
        self.client_admin.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.especialidade = {
            "nome": 'Segurança',
            "descricao": 'Cuida da segurança do evento'
        }

        self.evento = {
            "nome": 'GrudeFest',
            "descricao": 'Evento das Comunidades de TI da Paraíba',
            "data": "2020-01-17",
            "local": 'Unipe'
        }

    def test_cadastrar_evento(self):
        response = self.client_candidato.post('/api/eventos/', self.evento, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cadastrar_especilidade_sem_permissao(self):
        response = self.client_candidato.post('/api/especialidades/', self.especialidade, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
