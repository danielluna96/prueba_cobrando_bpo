from django.db import models

class Departamento(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    presupuesto = models.FloatField()

    class Meta:
        db_table = 'departamento'