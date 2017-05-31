# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from perfiles.models import Cliente
from customs.models import Articulo
from customs.models import Empresa
from customs.models import Servicio
from django.db import models

# Create your models here.
class OrdenServicio(models.Model):

    id_servicio = models.ForeignKey(
        Servicio,
        on_delete=models.CASCADE,
        related_name="OrdenServicio",
        related_query_name="OrdenServicio",
        )
    id_cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="Cliente",
        related_query_name="Cliente",
        )
    id_empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name="Empresa",
        related_query_name="Empresa",
        )
    descuento = models.IntegerField(default=0)
    precio_orden= models.FloatField()
    cantidad_piezas = models.IntegerField(default=0)
    fecha_solicitud = models.DateTimeField(auto_now=False, auto_now_add=True)
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

    id_orden = models.ForeignKey(
        OrdenServicio,
        on_delete=models.CASCADE,
        related_name="OrdenServicio",
        related_query_name="OrdenServicio",
        )
    id_articulo = models.ForeignKey(
        Articulo,
        on_delete=models.CASCADE,
        related_name="Articulo",
        related_query_name="Articulo",)
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
