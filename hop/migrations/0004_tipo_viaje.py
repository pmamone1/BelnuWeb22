# Generated by Django 4.0.3 on 2022-03-07 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hop', '0003_empleados_alter_hop_cant_acomp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Viaje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('Camion Drop Off', 'Camion Drop Off'), ('Sprinter Drop Off', 'Sprinter Drop Off'), ('Sprinter Pick Up', 'Sprinter Pick Up')], max_length=60, verbose_name='Tipo de Viaje:')),
                ('valor_viaje', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor del Viaje:')),
            ],
        ),
    ]
