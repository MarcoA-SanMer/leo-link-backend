# Generated by Django 5.0.7 on 2024-09-23 04:46

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_notificacion_tipo_e'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='fecha_fin_descuento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.user_image_upload_path),
        ),
    ]
