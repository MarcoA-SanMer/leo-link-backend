# Generated by Django 5.0.7 on 2024-09-30 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_evento_acceso_e'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
