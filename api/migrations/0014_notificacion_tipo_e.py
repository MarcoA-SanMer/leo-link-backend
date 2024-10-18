# Generated by Django 5.0.7 on 2024-09-16 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_categoriaevento_tipo_e'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacion',
            name='tipo_e',
            field=models.CharField(choices=[('evento', 'Evento'), ('practica', 'Práctica Profesional'), ('beneficio', 'Beneficio'), ('descuento', 'Descuento')], default='evento', max_length=20),
        ),
    ]
