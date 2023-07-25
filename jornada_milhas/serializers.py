from rest_framework import serializers
from jornada_milhas.models import Depoimento,Destino

class DepoimentosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Depoimento
        fields = '__all__'
    
class DestinosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = '__all__'
