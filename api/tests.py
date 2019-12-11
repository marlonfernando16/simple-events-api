from django.test import TestCase
from api import models
from model_mommy import mommy
import datetime


class UserTestCase(TestCase):
    def setUp(self):
        self.usuario = mommy.make(models.User, username='mfive', nome='Marlon', telefone=99999999,
                                email='mfive.com', data_nascimento="1998-08-03")
        self.usuario.set_password('123')
        self.usuario.save()

    def test_login(self):
        self.client.login(username=self.usuario.username, password='123')


class EventoTestCase(UserTestCase):

    def test_cadastrar_evento(self):
        self.evento = mommy.make(
            models.Evento,
            nome='GrudeFest',
            descricao='Evento das Comunidades de TI da Paraíba',
            owner=self.usuario,
            data=datetime.datetime.now(),
            local='Unipe',
            finalizado=False
        )
        self.assertTrue(self.evento.id > 0)
