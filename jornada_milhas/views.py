from rest_framework import viewsets
from jornada_milhas.models import Depoimento
from jornada_milhas.serializers import DepoimentosSerializers

class DepoimentosViewSet(viewsets.ModelViewSet):
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentosSerializers