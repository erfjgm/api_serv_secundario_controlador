from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
import datetime
from ticadas.models import Ticada
from ticadas.serializers import TicadaSerializer

class TicadasViewSet(viewsets.ModelViewSet):
    queryset = Ticada.objects.filter(delete_at__isnull=True)
    serializer_class = TicadaSerializer

    def destroy(self, request, *args, **Kargs):
        instance = self.get_object()
        instance.delete_at = datetime.datetime.now()
        instance.save()
        return Response(
            {"message": "Eliminado correctamente"},
            status=status.HTTP_200_OK
        )

