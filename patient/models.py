from django.db import models

class Patients(models.Model):
    id_patient = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=80, blank=False, null=False)
    number_address = models.IntegerField()
    neighborhood = models.CharField(max_length=60, blank=False, null=False)
    zip_code = models.CharField(max_length=100, blank=False, null=False)
    date_register = models.DateField(auto_now_add=True)
    rg = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'patients'
        