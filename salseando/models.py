from django.db import models

# Create your models here.
class gruposalsa(models.Model):
    title = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    ndiscos = models.SmallIntegerField()
    imagen = models.CharField(max_length=500)
