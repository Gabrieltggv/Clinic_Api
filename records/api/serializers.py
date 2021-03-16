from rest_framework import serializers
from images.api.serializers import ImagesHistoricalSerializer

from records.models import Records

class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = '__all__'
        

class RecordsDetailsSerializer(serializers.ModelSerializer):
    images = ImagesHistoricalSerializer(many=True, read_only=True)
    
    class Meta:
        model = Records
        fields = [
            'id_historic',
            'date',
            'appearance_symptoms',
            'local_pain',
            'kind_pain',
            'conclusion',
            'images'

        ]