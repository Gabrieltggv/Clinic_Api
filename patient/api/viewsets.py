from rest_framework import viewsets

from patient.models import Patients
from patient.api.serializers import PatientsSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
from patient.api.serializers import PatientsDetailsSerializer

class PatientsViewset(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializers

    @action(detail=True, methods=['get'])
    def details(self, resquest, pk=None, *args, **kwargs):
        queryset = Patients.objects.filter(pk=pk)
        self.serializer_class = PatientsDetailsSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
