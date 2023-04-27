from rest_framework import viewsets
from prueba_cobrando_bpo.personas.models import Empleado

from prueba_cobrando_bpo.personas.serializers import EmpleadoSerializer, EmpleadoUpdateSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'partial_update':
            return EmpleadoUpdateSerializer
        return EmpleadoSerializer