from .models import *
from perfiles.serializers import *
from ordenes.serializers import *
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apirest import *
import datetime
import json
from django.shortcuts import HttpResponse

class ClausulaApi(GenericMixin):
    queryset = Clausula.objects.all()
    serializer_class = ClausulaSerializer

class ConfiguracionApi(GenericMixin):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer

class EmpresaApi(GenericMixin):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class RecepcionApi(GenericMixin):
    queryset = Recepcion.objects.all()
    serializer_class = RecepcionSerializer

class RecomendadoApi(GenericMixin):
    queryset = Recomendado.objects.all()
    serializer_class = RecomendadoSerializer

class ServicioApi(GenericMixin):
    queryset = Servicio.objects.all()
    serializer_class =  ServicioSerializer

class ClienteApi(GenericMixin):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class DireccionClienteApi(GenericMixin):
    queryset = DireccionCliente.objects.all()
    serializer_class = DireccionClienteSerializer

class RechazaClausulaApi(GenericMixin):
    queryset = RechazaClausula.objects.all()
    serializer_class =  RechazaClausulaSerializer

class ArticuloApi(GenericMixin):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

class ServicioApi(GenericMixin):
    queryset = Servicio.objects.all()
    serializer_class =  ServicioSerializer

class CodbarraArticuloApi(GenericMixin):
    queryset = CodbarraArticulo.objects.all()
    serializer_class = CodbarraArticuloSerializer

class OrdenServicioApi(GenericMixin):
    queryset = OrdenServicio.objects.all()
    serializer_class = OrdenServicioSerializer
