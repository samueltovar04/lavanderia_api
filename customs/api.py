from perfiles.models import *
from .models import *
from rest_framework import views, serializers, generics, filters, permissions, status, mixins
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from perfiles.serializers import *
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import datetime
import json
from django.shortcuts import HttpResponse

class PermissionMixin(object):
    permission_classes = (permissions.IsAdminUser,)

class GenericMixin(PermissionMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        if 'pk' not in kwargs:
            return self.list(request, *args, **kwargs)
        else:
            return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):

        self.object = self.get_object_or_none()
        serializer = self.get_serializer(self.object, data=request.DATA,files=request.FILES, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            self.pre_save(serializer.object)
        except ValidationError as err:
            return Response(err.message_dict, status=status.HTTP_400_BAD_REQUEST)
        if self.object is None:
            self.object = serializer.save(force_insert=True)
            self.post_save(self.object, created=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        self.object = serializer.save(force_update=True)
        self.post_save(self.object, created=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter = {}
        fields = tuple([str(x.name) for x in self.queryset.model._meta.fields])
        for key,value in self.request.query_params.dict().items():
            key_split = key.split('__')[0]
            if key_split in fields:
                if value.lower() == 'true':
                    value = True
                elif value.lower() == 'false':
                    value = False
                filter.update({key:value})
        try:
            filtered_object = queryset.filter(**filter)
        except:
            filtered_object = queryset
        serializer = eval("%sSerializer(filtered_object, many=True)"%(self.__class__.__name__[:-3],))
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = self.get_queryset().get(pk=pk)
        serializer = eval("%sSerializer(queryset)"%(self.__class__.__name__[:-3],))
        return Response(serializer.data)

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

