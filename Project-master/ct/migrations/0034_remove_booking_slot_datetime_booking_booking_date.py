# Generated by Django 4.2.5 on 2023-11-03 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ct', '0033_doctorprofile_booked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='slot_datetime',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(default=None),
        ),
    ]
