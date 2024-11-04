# Generated by Django 4.2.5 on 2023-11-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ct', '0052_timeslot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='session',
            field=models.CharField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')], max_length=20),
        ),
    ]
