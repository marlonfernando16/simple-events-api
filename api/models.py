from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nome = models.CharField(verbose_name="Nome", max_length=255, blank=False)
    telefone = models.CharField(verbose_name="Telefone", max_length=255, blank=False)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento", blank=False)
    admin = models.BooleanField(verbose_name='Status de Admin', default=False)

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Evento(models.Model):
    nome = models.CharField(max_length=255, blank=False)
    descricao = models.CharField(max_length=255, blank=False)
    owner = models.ForeignKey(
        User,
        verbose_name="Proprietário",
        related_name="eventos",
        on_delete=models.CASCADE,
        blank=False
    )
    data = models.DateField(verbose_name="Data", blank=False)
    local = models.CharField(verbose_name="Local", max_length=255, blank=False)
    finalizado = models.NullBooleanField()

    def __str__(self):
        return self.nome


class Especialidade(models.Model):
    nome = models.CharField(max_length=255, blank=False, unique=True)
    descricao = models.CharField(max_length=255, blank=False)

    class Meta:
        verbose_name = u'Modelo de Especialidade'
        verbose_name_plural = u'Modelo de Especialidades'

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    evento = models.ForeignKey(
        Evento,
        verbose_name="Evento",
        related_name="vagas",
        on_delete=models.CASCADE
    )
    qtd_vagas = models.PositiveIntegerField(verbose_name="Quantidade de Vagas", blank=False)
    especialidade = models.ForeignKey(
        Especialidade,
        verbose_name='Especialidades',
        related_name='vagas',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.especialidade.nome


class CandidatoVaga(models.Model):
    DEFERIDO = "DEFERIDO"
    INDEFERIDO = "INDEFERIDO"
    NAOAVALIADO = "NAOAVALIADO"
    TIPO_CHOICES = (
        (1, DEFERIDO),
        (2, INDEFERIDO),
        (3, NAOAVALIADO)
    )

    candidato = models.OneToOneField(User, verbose_name="Candidato", on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, verbose_name="Vaga", related_name="candidatos_vaga", on_delete=models.CASCADE)
    nota_desempenho = models.PositiveIntegerField(verbose_name="Nota  de Desempenho", blank=True, null=True)
    state_vaga = models.PositiveSmallIntegerField(verbose_name="Status da Vaga", choices=TIPO_CHOICES)

    def __str__(self):
        return self.candidato.nome


class AvaliacaoEvento(models.Model):
    evento = models.ForeignKey(
        Evento,
        verbose_name="Evento",
        related_name="avaliacoes_evento",
        on_delete=models.CASCADE
    )
    nota_avaliacao_evento = models.DecimalField(
        verbose_name="Nota da Avaliação",
        decimal_places=1,
        max_digits=2,
        blank=True,
        null=True
    )