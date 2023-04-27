from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Departamento(models.Model):
    codigo = models.BigIntegerField(
        primary_key=True, 
        validators=[
            MinValueValidator(0),
            MaxValueValidator(9999999999)
            ]
    )   
    nombre = models.CharField(max_length=100)
    presupuesto = models.FloatField()

    class Meta:
        db_table = 'departamento'