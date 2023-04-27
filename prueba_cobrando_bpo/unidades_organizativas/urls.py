from rest_framework.routers import DefaultRouter
from prueba_cobrando_bpo.unidades_organizativas.views import DepartamentoViewSet

router = DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet)
urlpatterns = router.urls
