# Generated by Django 4.1.4 on 2023-03-06 00:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('maquinaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquinaria',
            name='fecha_compra_maquinaria',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
