# Generated by Django 4.1.4 on 2023-01-27 05:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='edad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_de_ingreso',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]