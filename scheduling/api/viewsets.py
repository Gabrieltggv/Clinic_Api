from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from scheduling.models import Appointments
from scheduling.api.serializers import AppointmentsSerializer, AppointmentsDetailsSerializer

class AppointmentsViewSet(viewsets.ModelViewSet):
    queryset = Appointments.objects.all().order_by('date_time')
    serializer_class = AppointmentsSerializer

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None, *args, **kwargs):
        queryset = Appointments.objects.filter(pk=pk)
        self.serializer_class = AppointmentsDetailsSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
    