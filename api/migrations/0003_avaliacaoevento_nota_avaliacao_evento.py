# Generated by Django 2.2.4 on 2019-09-03 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_avaliacaoevento_nota_avaliacao_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacaoevento',
            name='nota_avaliacao_evento',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Nota da Avaliação'),
        ),
    ]