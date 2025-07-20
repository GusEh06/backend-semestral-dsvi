from rest_framework import viewsets
from .models import Visitante, RegistroVisita
from .serializers import VisitanteSerializer,RegistroVisitaSerializer


class VisitanteViewSet(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()
    serializer_class = VisitanteSerializer

class RegistroVisitaViewSet(viewsets.ModelViewSet):
    queryset = RegistroVisita.objects.all()
    serializer_class = RegistroVisitaSerializer
