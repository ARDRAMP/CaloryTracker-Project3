# Generated by Django 4.2.5 on 2024-03-01 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ct', '0076_video_created_at_video_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='updated_at',
        ),
    ]
