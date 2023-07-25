from rest_framework import viewsets
from jornada_milhas.models import Depoimento,Destino
from jornada_milhas.serializers import DepoimentosSerializers,DestinosSerializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import random 

class Authentication(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class DepoimentosViewSet(Authentication,viewsets.ModelViewSet):
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentosSerializers

class DepoimentosHomeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DepoimentosSerializers
    http_method_names = ['get']

    def get_queryset(self):
        depoimentos = Depoimento.objects.all()
        queryset = random.sample(list(depoimentos), k=3)
        return queryset

class DestinosViewSet(Authentication,viewsets.ModelViewSet):
    queryset = Destino.objects.all()
    serializer_class = DestinosSerializers



