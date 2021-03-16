from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from records.api.serializers import RecordsSerializer
from records.api.serializers import RecordsDetailsSerializer
from records.models import Records

class RecordsViewSet(viewsets.ModelViewSet):
    queryset = Records.objects.all().order_by('date')
    serializer_class = RecordsSerializer

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None, *args, **kwargs):
        queryset = Records.objects.filter(pk=pk)
        self.serializer_class = RecordsDetailsSerializer
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
