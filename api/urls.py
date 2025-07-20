from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VisitanteViewSet, RegistroVisitaViewSet

router = DefaultRouter()
router.register(r'visitantes', VisitanteViewSet)
router.register(r'registro_visitas', RegistroVisitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
