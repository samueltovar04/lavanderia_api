# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Clausula(models.Model):

    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    status = models.IntegerField(default=1)
    class Meta:
        db_table = 'clausulas'

    def __unicode__(self):
        return self.descripcion

class Configuracion(models.Model):

    codigo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    valor = models.FloatField()
    status = models.IntegerField(default=1)
    class Meta:
        db_table = 'configuraciones'

    def __unicode__(self):
        return self.descripcion

class Empresa(models.Model):

    nit = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    sucursal = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=200)
    web = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    status = models.IntegerField(default=1)
    class Meta:
        db_table = 'empresas'

    def __unicode__(self):
        return self.descripcion

class Recepcion(models.Model):

    descripcion = models.CharField(max_length=200)
    activo = models.IntegerField(default=1)
    class Meta:
        db_table = 'recepciones'

    def __unicode__(self):
        return self.descripcion

class Recomendado(models.Model):

    cedula = models.BigIntegerField()
    nombre = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.IntegerField(default=0)
    class Meta:
        db_table = 'recomendados'

    def __unicode__(self):
        return self.nombre

class Servicio(models.Model):

    descripcion = models.CharField(max_length=200)
    status = models.IntegerField(default=1)
    class Meta:
        db_table = 'servicios'

    def __unicode__(self):
        return self.descripcion

class Articulo(models.Model):

    descripcion = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    status = models.IntegerField(default=1)
    class Meta:
        db_table = 'articulos'

    def __unicode__(self):
        return self.descripcion





















