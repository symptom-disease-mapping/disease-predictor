from django.shortcuts import render
from rest_framework import status
# Create your views here. 
from rest_framework.views import APIView 
from rest_framework.decorators import api_view
from . models import Info
from rest_framework.response import Response 
from . serializer import *
from .serializer import InfoSerializer
from .models import *
from .serializer import SympDiseaseSerializer
from .serializer import SympSearchSerializer
from .serializer import *
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
    serializer_class = MajorSympSerializer
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
        symptom = symptom+"\r"
        print(symptom)
  
        try:
            ms1 = MajorSymptoms.objects.get(ms_name__exact=symptom)
            print(symptom)
            #MajorSymptoms.objects.filter(ms_name__icontains="fever").update(ms_name="Fever")
            
            serializer1 = MajorSympSerializer(ms1)
            ms_id = ms1.ms_id
            precise = MorePreciseSymptoms.objects.filter(link_1=ms_id)
            serializer2 = MorePreSympSerializer(precise,many=True)
            #link_1=precise.link_1
            # return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer2.data, status=status.HTTP_200_OK)
            #return Response({'ms_id': ms_id}, status=status.HTTP_200_OK)
        except MorePreciseSymptoms.DoesNotExist:
            return Response({'error': 'Disease not found'}, status=status.HTTP_404_NOT_FOUND)
    def get(self, request, *args, **kwargs):
        # Your logic to handle GET requests
        # For example, fetching all diseases or some initial data
        diseases = MajorSymptoms.objects.all()
        serializer = MajorSympSerializer(diseases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class MajorSymp(APIView):
     def post(self, request, *args, **kwargs):
        symptom = request.data.get('symptom')

        try:
            disease = SympDisease.objects.get(symptom=symptom.strip())
            
            serializer = SympSearchSerializer(disease)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except MajorSymptoms.DoesNotExist:
            return Response({'error': 'Disease not found'}, status=status.HTTP_404_NOT_FOUND)
     def get(self, request, *args, **kwargs):
        # Your logic to handle GET requests
        # For example, fetching all diseases or some initial data
        diseases = SympDisease.objects.all()
        serializer = SympSearchSerializer(diseases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)