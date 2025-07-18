from rest_framework import viewsets
from .models import Visitante
from .serializers import VisitanteSerializer


class VisitanteViewSet(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()
    serializer_class = VisitanteSerializer
