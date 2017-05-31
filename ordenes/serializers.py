from rest_framework import serializers
from .models import *

class OrdenServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenServicio
        fields = '__all__'

class CodbarraArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodbarraArticulo
        fields = '__all__'

