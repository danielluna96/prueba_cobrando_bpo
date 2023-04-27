from rest_framework import viewsets
from prueba_cobrando_bpo.unidades_organizativas.models import Departamento

from prueba_cobrando_bpo.unidades_organizativas.serializers import DepartamentoSerializer, DepartamentoUpdateSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'partial_update':
            return DepartamentoUpdateSerializer
        return DepartamentoSerializer