# Generated by Django 4.2.5 on 2023-10-27 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ct', '0023_remove_userprofile_bio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='height',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
