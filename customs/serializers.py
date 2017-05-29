from rest_framework import serializers
from .models import *

class ClausulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clausula
        fields = ('id','titulo','descripcion','status')

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class RecepcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recepcion
        fields = '__all__'

class RecomendadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendado
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'
