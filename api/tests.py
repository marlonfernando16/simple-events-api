from django.test import TestCase
from api.models import User
from model_mommy import mommy


class UserTestCase(TestCase):
    def setUp(self):
        self.usuario = mommy.make(User, username='mfive', nome='Marlon', telefone=99999999,
                                email='mfive.com', data_nascimento="1998-08-03")
        self.usuario.set_password('123')
        self.usuario.save()

    def test_login(self):
        self.client.login(username=self.usuario.username, password='123')



