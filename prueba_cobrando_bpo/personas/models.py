from django.db import models

class Empleado(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    nit = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    codigo_departamento = models.ForeignKey('unidades_organizativas.Departamento', on_delete=models.CASCADE)

    class Meta:
        db_table = 'empleado'
