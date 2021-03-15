from rest_framework import serializers
from patient.models import Patients
from scheduling.api.serializers import AppointmentsDetailsSerializer

class PatientsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'

class PatientsDetailsSerializer(serializers.ModelSerializer):
    appointments = AppointmentsDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Patients
        fields = [
            'id_patient',
            'name', 
            'date_of_birth',
            'address',
            'number_address',
            'neighborhood',
            'zip_code',
            'date_register',
            'rg',
            'appointments'
        ]