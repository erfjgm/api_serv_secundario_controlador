from django.db import models

# Create your models here.

class Ticada(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    controlador = models.CharField(max_length=12)
    llave = models.CharField(max_length=12)
    delete_at = models.DateField(null=True, blank=True)