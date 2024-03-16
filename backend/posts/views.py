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

class getMajorSymptoms(APIView):
    def get(self, request, *args, **kwargs):
        majorSymptoms = MajorSymptoms.objects.all().values('ms_name')
        # serializer = MajorSympSerializer(majorSymptoms, many=True)
        list = [item['ms_name'] for item in majorSymptoms]
        return Response(list, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        symptoms = request.data.get('symptoms',[])
        print(symptoms)
        preSympList=[]
        ms_ids=[]
        for symptom in symptoms:
         symptom = symptom+"\r"
         print(symptom)
  
         try:
            ms1 = MajorSymptoms.objects.get(ms_name__exact=symptom)
            print(symptom)
            serializer1 = MajorSympSerializer(ms1)
            ms_id = ms1.ms_id
            ms_ids.append(ms_id)
            
            precise = MorePreciseSymptoms.objects.filter(link_1=ms_id)
            serializer2 = MorePreSympSerializer(precise,many=True)
            # preSympId = [id['mps_id'] for id in serializer2.data]
            preSympList.extend(item['mps_name'] for item in serializer2.data)
        
         except MorePreciseSymptoms.DoesNotExist:
            return Response({'error': 'Disease not found'}, status=status.HTTP_404_NOT_FOUND)
        request.session['ms_ids']= ms_ids
        print(ms_ids)
        return Response(preSympList, status=status.HTTP_200_OK)
        
class getPreciseSymptoms(getMajorSymptoms):
    def post(self, request, *args, **kwargs):
        preSymps = request.data.get('preSymps',[])
        result = []
        mps_ids=[]
        for preSymp in preSymps:
         try:
            mps = MorePreciseSymptoms.objects.get(mps_name=preSymp)
            serializer = MorePreSympSerializer(mps)
            mps_id = mps.mps_id
            mps_ids.append(mps_id)
            
            result.append(serializer.data)
            
         except MorePreciseSymptoms.DoesNotExist:
            result.append({'error': f'Disease not found for {preSymp}'})
        request.session['mps_id'] = mps_ids
        return Response(result, status=status.HTTP_200_OK)
    def get(self, request, *args, **kwargs):
        diseases = MorePreciseSymptoms.objects.all()
        serializer = MorePreSympSerializer(diseases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)   
class getDiseases(getPreciseSymptoms):
    
    def post(self, request, *args, **kwargs):
        ms_ids = request.session.get('ms_ids')
        print(ms_ids)
        diseases=[]
        for ms_id in ms_ids:
            disease_obj = Diseases.objects.filter(major_symptom__exact = ms_id)
            for disease in disease_obj:
             disease_name = disease.d_name
             diseases.append(disease_name)
        return Response(diseases, status=status.HTTP_200_OK)
