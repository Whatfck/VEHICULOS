from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    COLOR=(
        ('1', 'Blanco'),
        ('2', 'Negro'),
        ('3', 'Rojo'),
        ('4', 'Azul'),
        ('5', 'Amarillo'),
        
    )
    placa=models.CharField(max_length=6)
    marca=models.CharField(max_length=10)
    color_vehiculo=models.CharField('color' ,max_length=1,choices=COLOR)
    modelo=models.IntegerField()

    def __str__(self):
        return self.placa