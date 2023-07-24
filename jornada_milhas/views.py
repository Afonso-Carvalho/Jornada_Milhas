from rest_framework import viewsets,status
from jornada_milhas.models import Depoimento
from rest_framework.response import Response
from jornada_milhas.serializers import DepoimentosSerializers
import random 


class DepoimentosViewSet(viewsets.ModelViewSet):
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentosSerializers

class DepoimentosHomeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DepoimentosSerializers
    http_method_names = ['get']

    def get_queryset(self):
        depoimentos = Depoimento.objects.all()
        queryset = random.sample(list(depoimentos), k=3)
        return queryset


