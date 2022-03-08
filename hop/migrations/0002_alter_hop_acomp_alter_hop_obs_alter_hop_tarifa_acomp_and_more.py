# Generated by Django 4.0.3 on 2022-03-07 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hop',
            name='acomp',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Acompañante:'),
        ),
        migrations.AlterField(
            model_name='hop',
            name='obs',
            field=models.TextField(blank=True, max_length=500, verbose_name='Observaciones:'),
        ),
        migrations.AlterField(
            model_name='hop',
            name='tarifa_acomp',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Tarifa Acompañante:'),
        ),
        migrations.AlterField(
            model_name='hop',
            name='tarifa_camion',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Tarifa Camion:'),
        ),
        migrations.AlterField(
            model_name='hop',
            name='tipo',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Tipo Viaje:'),
        ),
    ]
