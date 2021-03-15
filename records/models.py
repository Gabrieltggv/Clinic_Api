from django.db import models
from scheduling.models import Appointments

# Create your models here.
class Records(models.Model):
    id_historic = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    appearance_symptoms = models.CharField(max_length=100, blank=True, null=True)
    duration_symptoms = models.CharField(max_length=100, blank=True, null=True)
    local_pain = models.CharField(max_length=100, blank=True, null=True)
    kind_pain = models.CharField(max_length=100, blank=True, null=True)
    conclusion = models.CharField(max_length=100, blank=True, null=True)
    id_scheduling = models.ForeignKey(Appointments, related_name='records', on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'records'
