from rest_framework import serializers
from prueba_cobrando_bpo.personas.models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class EmpleadoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        exclude = ['codigo']