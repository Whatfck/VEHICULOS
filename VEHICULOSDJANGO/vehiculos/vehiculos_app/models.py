from django.db import models

# Create your models here.
class vehicle(models.Model):
    COLOR=(
        ('1', 'ROJO')
        ('2', 'AZUL')
        ('3', 'VERDE')
        ('4', 'NEGRO')
        ('5', 'VIOLETA')
        ('6', 'ROSADO')
        ('7', 'AMARILLO')
        ('8', 'GRIS')
    )

    placa=models.CharField(max_length=6)
    marca=models.CharField(max_length=10)
    color_vehiculo=models.CharField('color',max_length=1,choices=COLOR)
    modelo=models.IntegerField()

    def __str__(self):
        return self.placa
    