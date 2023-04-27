from rest_framework import serializers
from prueba_cobrando_bpo.unidades_organizativas.models import Departamento

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class DepartamentoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        exclude = ['codigo']
