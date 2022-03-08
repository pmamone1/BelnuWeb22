# Generated by Django 4.0.3 on 2022-03-07 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hop', '0005_alter_tipo_viaje_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hop',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Camion Drop Off', 'Camion Drop Off'), ('Sprinter Drop Off', 'Sprinter Drop Off'), ('Sprinter Pick Up', 'Sprinter Pick Up')], max_length=30, null=True, verbose_name='Tipo Viaje:'),
        ),
    ]
