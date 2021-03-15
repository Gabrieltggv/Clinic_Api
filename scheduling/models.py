from django.db import models
from patient.models import Patients

# Create your models here.
class Appointments(models.Model):
    id_scheduling = models.AutoField(primary_key=True)
    date_time = models.DateField(blank=False, null=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    canceled = models.BooleanField(default=False)
    obs = models.TextField(blank=True, null=True)
    kind = models.CharField(max_length=100, blank=True, null=True)
    id_patient = models.ForeignKey(Patients, on_delete=models.CASCADE, related_name='appointments', blank=False, null=False)
    
    class Meta:
        managed = True
        db_table = 'Appointments'
        unique_together = ('date_time', 'id_patient')
        