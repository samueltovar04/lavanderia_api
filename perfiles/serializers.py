from rest_framework import serializers
from .models import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class DireccionClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DireccionCliente
        fields = '__all__'

class RechazaClausulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RechazaClausula
        fields = '__all__'
