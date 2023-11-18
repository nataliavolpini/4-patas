from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perro(models.Model):

    nombre = models.CharField(max_length=64)
    raza =  models.CharField(max_length=64, blank=True)  
    fecha_nacimiento = models.DateField(null=True)
    descripcion = models.CharField(max_length=256)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)#linea creador

    def __str__(self):
        return f'{self.nombre} ({self.raza})'
    
