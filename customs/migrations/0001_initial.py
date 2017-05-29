# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('categoria', models.CharField(max_length=200)),
                ('status', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'articulos',
            },
        ),
        migrations.CreateModel(
            name='Clausula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('status', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'clausulas',
            },
        ),
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('valor', models.FloatField()),
                ('status', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'configuraciones',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=200)),
                ('sucursal', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=200)),
                ('web', models.CharField(max_length=200)),
                ('ubicacion', models.CharField(max_length=200)),
                ('status', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'empresas',
            },
        ),
        migrations.CreateModel(
            name='Recepcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('activo', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'recepciones',
            },
        ),
        migrations.CreateModel(
            name='Recomendado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.BigIntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'recomendados',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('status', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'servicios',
            },
        ),
    ]
