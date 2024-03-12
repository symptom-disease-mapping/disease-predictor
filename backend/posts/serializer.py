from rest_framework import serializers 
from . models import Info
from .models import SympDisease
from .models import *

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

class MajorSympSerializer(serializers.ModelSerializer):
    class Meta:
        model = MajorSymptoms
        fields = ['ms_id','ms_name']

class MorePreSympSerializer(serializers.ModelSerializer):
    class Meta:
        model = MorePreciseSymptoms
        fields = ['mps_name','link_1']