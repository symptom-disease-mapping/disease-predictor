# Generated by Django 5.0.3 on 2024-03-21 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_vitalinfo_disease_vitalinfo_aadhar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vitalinfo',
            name='Disease',
        ),
    ]
