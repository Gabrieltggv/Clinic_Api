from rest_framework import viewsets
from images.models import ImagesHistorical
from images.api.serializers import ImagesHistoricalSerializer


class ImagesHistoricalViewSet(viewsets.ModelViewSet):
    queryset = ImagesHistorical.objects.all()
    serializer_class = ImagesHistoricalSerializer
    