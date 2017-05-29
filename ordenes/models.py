# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from perfil.models import Cliente
from custom.models import Articulo
from custom.models import Empresa
from custom.models import Servicio
from django.db import models
import datetime
# Create your models here.
class OrdenServicio(models.Model):

    id_servicio = models.ForeignKey(Servicio, related_name='id_servicio')
    id_cliente = models.ForeignKey(Cliente, related_name='id_cliente')
    id_empresa = models.ForeignKey(Empresa, related_name='id_empresa')
    descuento = models.IntegerField(default=0)
    precio_orden= models.FloatField()
    cantidad_piezas = models.IntegerField(default=0)
    fecha_solicitud = models.DateTimeField(Datetime.auto_now=True)
    fecha_entrega = models.DateTimeField(null=True)
    recepcion = models.CharField(max_length=200)
    forma_entrega = models.CharField(max_length=200)
    observacion = models.CharField(max_length=200)
    status = models.IntegerField(default=1)
    class Meta:
        db_table = 'orden_servicios'
    def __unicode__(self):
        return self.id_cliente

class CodbarraArticulo(models.Model):

    id_orden = models.ForeignKey(Articulo, related_name='id_articulo')
    id_articulo = models.ForeignKey(Articulo, related_name='id_articulo')
    codigo_barra = models.CharField(max_length=30)
    categoria = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    observacion = models.CharField(max_length=200)
    status = models.IntegerField(default=1)
    class Meta:
        db_table = 'codbarra_articulos'
        unique_together = (("id_articulo", "id_orden","codigo_barra"),)

    def __unicode__(self):
        return self.codigo_barra
