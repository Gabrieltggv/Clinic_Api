from rest_framework import viewsets
from records.api.serializers import RecordsSerializer
from records.models import Records

class RecordsViewSet(viewsets.ModelViewSet):
    queryset = Records.objects.all().order_by('date')
    serializer_class = RecordsSerializer
    