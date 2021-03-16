from rest_framework import serializers
from scheduling.models import Appointments
from records.api.serializers import RecordsDetailsSerializer
class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = '__all__'

        
class AppointmentsDetailsSerializer(serializers.ModelSerializer):
    records = RecordsDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Appointments
        fields = [
            'id_scheduling',
            'date_time',
            'date_creation',
            'canceled',
            'obs',
            'kind',
            'records'
        ]
