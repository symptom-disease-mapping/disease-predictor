from django.db import models

# Create your models here.
class Info(models.Model):
    age = models.IntegerField
    gender = models.CharField(max_length = 20)

class SympDisease(models.Model):
    symptom = models.CharField(max_length = 20, null = True)
    disease = models.CharField(max_length = 20)