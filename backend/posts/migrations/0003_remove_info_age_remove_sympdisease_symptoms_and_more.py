# Generated by Django 4.2.4 on 2024-03-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_sympdisease'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='age',
        ),
        migrations.RemoveField(
            model_name='sympdisease',
            name='symptoms',
        ),
        migrations.AddField(
            model_name='sympdisease',
            name='symptom',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sympdisease',
            name='disease',
            field=models.CharField(max_length=20),
        ),
    ]