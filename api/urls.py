from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VisitanteViewSet

router = DefaultRouter()
router.register(r'visitantes', VisitanteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
