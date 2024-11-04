# Generated by Django 4.2.5 on 2023-11-12 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ct', '0047_dietitianprofile_image_doctorprofile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterField(
            model_name='feedback',
            name='dietitian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ct.dietitianprofile'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ct.doctorprofile'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='professional_type',
            field=models.CharField(choices=[('Doctor', 'Doctor'), ('Dietitian', 'Dietitian')], max_length=20),
        ),
    ]
