# Generated by Django 2.2.4 on 2019-12-02 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191202_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='data_nascimento',
            field=models.DateField(verbose_name='Data de Nascimento'),
        ),
    ]
