from rest_framework import serializers
from images.models import ImagesHistorical


class ImagesHistoricalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesHistorical
        fields = '__all__'
        