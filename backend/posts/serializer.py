from rest_framework import serializers 
from . models import Info
from .models import SympDisease

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['age','gender']

class SympDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SympDisease
        fields = ['symptom','disease']

class SympSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SympDisease
        fields = ['symptom','disease']