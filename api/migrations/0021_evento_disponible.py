# Generated by Django 5.0.7 on 2024-10-15 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_customuser_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
    ]
