from rest_framework import serializers
from jornada_milhas.models import Depoimento

class DepoimentosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Depoimento
        fields = '__all__'
    