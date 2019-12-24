# Generated by Django 2.2.4 on 2019-12-24 22:30

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=255, verbose_name='Telefone')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('admin', models.BooleanField(default=False, verbose_name='Status de Admin')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('descricao', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Modelo de Especialidade',
                'verbose_name_plural': 'Modelo de Especialidades',
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('data', models.DateField(verbose_name='Data')),
                ('local', models.CharField(max_length=255, verbose_name='Local')),
                ('finalizado', models.NullBooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to=settings.AUTH_USER_MODEL, verbose_name='Proprietário')),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd_vagas', models.PositiveIntegerField(verbose_name='Quantidade de Vagas')),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vagas', to='api.Especialidade', verbose_name='Especialidades')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vagas', to='api.Evento', verbose_name='Evento')),
            ],
        ),
        migrations.CreateModel(
            name='CandidatoVaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota_desempenho', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota  de Desempenho')),
                ('state_vaga', models.PositiveSmallIntegerField(choices=[(1, 'DEFERIDO'), (2, 'INDEFERIDO'), (3, 'NAOAVALIADO')], verbose_name='Status da Vaga')),
                ('candidato', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Candidato')),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidatos_vaga', to='api.Vaga', verbose_name='Vaga')),
            ],
        ),
        migrations.CreateModel(
            name='AvaliacaoEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota_avaliacao_evento', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Nota da Avaliação')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes_evento', to='api.Evento', verbose_name='Evento')),
            ],
        ),
    ]
