from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Empleado(models.Model):
    codigo = models.BigIntegerField(
        primary_key=True, 
        validators=[
            MinValueValidator(0),
            MaxValueValidator(9999999999)
            ]
    ) 
    nit = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    codigo_departamento = models.ForeignKey('unidades_organizativas.Departamento', on_delete=models.CASCADE)

    class Meta:
        db_table = 'empleado'
