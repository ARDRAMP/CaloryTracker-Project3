# Generated by Django 4.2.5 on 2023-11-07 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ct', '0046_feedback_dietitian_feedback_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='dietitianprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dietitian_images/'),
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='doctor_images/'),
        ),
    ]
