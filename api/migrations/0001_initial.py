# Generated by Django 5.0.2 on 2024-02-23 17:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('idcolaborador', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=45)),
                ('edad', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('profesion', models.CharField(max_length=45)),
                ('estadocivil', models.CharField(max_length=45)),
            ],
        ),
    ]