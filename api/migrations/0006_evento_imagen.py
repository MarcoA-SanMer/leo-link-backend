# Generated by Django 5.0.7 on 2024-09-01 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_asistencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='event_images/'),
        ),
    ]
