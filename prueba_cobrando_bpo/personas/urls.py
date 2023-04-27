from rest_framework.routers import DefaultRouter
from prueba_cobrando_bpo.personas.views import EmpleadoViewSet

router = DefaultRouter()
router.register(r'empleados', EmpleadoViewSet)
urlpatterns = router.urls
