# Generated by Django 4.1.6 on 2023-05-06 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='end_time',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='appointment',
            name='start_time',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
