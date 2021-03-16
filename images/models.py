from django.db import models
from records.models import Records

# Create your models here.

def images_historical(instance, filename):
    return '/'.join(['historical', str(instance.id_historic.id_historic), filename])

class ImagesHistorical(models.Model):
    id_image_historical = models.AutoField(primary_key=True)
    image = models.ImageField(blank=True, null=True, upload_to=images_historical)
    id_historic = models.ForeignKey(Records, related_name='images', on_delete=models.CASCADE, blank=False, null=False)
