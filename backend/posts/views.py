from django.shortcuts import render
from rest_framework import status
# Create your views here. 
from rest_framework.views import APIView 
from rest_framework.decorators import api_view
from . models import Info
from rest_framework.response import Response 
# from . serializer import *
from .serializer import InfoSerializer
from .models import SympDisease
from .serializer import SympDiseaseSerializer
from .serializer import SympSearchSerializer
# Create your views here. 
  
class InfoView(APIView): 
    
    serializer_class = InfoSerializer 
  
    def get(self, request): 
        detail = [ {"age": detail.age,"gender": detail.gender}  
        for detail in Info.objects.all()] 
        return Response(detail) 
  
    def post(self, request): 
  
        serializer = InfoSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return  Response(serializer.data) 
        
    def receive_data(request):
    # Handle incoming data
      data = request.data
      return Response({'message': 'Data received successfully'})
    
class SympDiseaseView(APIView):
    serializer_class = SympDiseaseSerializer
    def get(self, request): 
        mapping = [ {"symptom": mapping.symptom,"disease": mapping.disease}  
        for mapping in SympDisease.objects.all()] 
        return Response(mapping) 
    
    def post(self, request): 
  
        serializer = SympDiseaseSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return Response(serializer.data)
 
class SearchDiseaseAPIView(APIView):
    def post(self, request, *args, **kwargs):
        symptom = request.data.get('symptom')

        try:
            disease = SympDisease.objects.get(symptom=symptom)
            serializer = SympSearchSerializer(disease)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SympDisease.DoesNotExist:
            return Response({'error': 'Disease not found'}, status=status.HTTP_404_NOT_FOUND)
    def get(self, request, *args, **kwargs):
        symptom = request.data.get('symptom')

        try:
            disease = SympDisease.objects.get(symptom=symptom)
            serializer = SympSearchSerializer(disease)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SympDisease.DoesNotExist:
            return Response({'error': 'Disease not found'}, status=status.HTTP_404_NOT_FOUND)