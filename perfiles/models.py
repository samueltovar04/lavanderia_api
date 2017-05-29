# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Cliente(models.Model):

    cedula = models.IntegerField(default=0)
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    sexo = models.CharField(max_length=1)
    telefono = models.CharField(max_length=200)
    movil = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    profesion = models.CharField(max_length=200)
    reg_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    password = models.CharField(max_length=40)
    status  = models.IntegerField(default=1)
    id_dispositivo = models.CharField(max_length=200)
    latitud = models.DecimalField(max_digits=10, decimal_places=7)
    longitud = models.DecimalField(max_digits=10, decimal_places=7)
    class Meta:
        db_table = 'clientes'

    def __unicode__(self):
        return self.fullname

class DireccionCliente(models.Model):

    id_cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="DireccionClientes",
        related_query_name="DireccionCliente",
    )
    pais  = models.CharField(max_length=100,default="Venezuela")
    estado  = models.CharField(max_length=100)
    ciudad  = models.CharField(max_length=100)
    direccion  = models.TextField()
    class Meta:
        db_table = 'direccion_cliente'
    def __unicode__(self):
            return "%s - %s"%(self.id_cliente,self.direccion)

class RechazaClausula(models.Model):
    id_cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="RechazaClausulas",
        related_query_name="RechazaClausula",
    )
    comentarios = models.TextField()
    fecha  = models.DateTimeField(auto_now=False, auto_now_add=True)
    contactado = models.IntegerField(default=0)
    class Meta:
        db_table = 'rechaza_clausula'
    def __unicode__(self):
        return self.id_cliente
