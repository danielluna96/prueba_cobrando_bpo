# Generated by Django 4.2 on 2023-04-27 15:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='codigo',
            field=models.BigIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
