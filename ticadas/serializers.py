from rest_framework import serializers
from ticadas.models import Ticada

class TicadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticada
        #fields ='__all__'
        exclude = ["delete_at"] 