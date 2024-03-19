from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from . serializer import *
from .models import *
from .serializer import *
import csv 
from django.shortcuts import get_object_or_404
# Create your views here.


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .tokens import generate_token
from backend import settings
from .models import AuthUser  # Import your custom user model

class Authentication(APIView):
    def get(self, request):
        return Response({'message': 'Choose an option', 'options': ['signup', 'signin']})

    def post(self, request):
        action = request.data.get('action')
        
        if action == 'signup':
            return self.signup(request)
        elif action == 'signin':
            return self.signin(request)
        else:
            return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)

    def signup(self, request):
        username = request.data.get('username')
        fname = request.data.get('fname')
        lname = request.data.get('lname')
        email = request.data.get('email')
        pass1 = request.data.get('pass1')
        pass2 = request.data.get('pass2')
        
        if not all([username, fname, lname, email, pass1, pass2]):
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
        
        if pass1 != pass2:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
        
        if AuthUser.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        if AuthUser.objects.filter(email=email).exists():
            return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = AuthUser.objects.create_user(username, email, pass1)
        user.first_name = fname
        user.last_name = lname
        user.is_active = False
        user.save()
        messages.success(request, "Your Account has been created successfully!! Please check your email to confirm your email address in order to activate your account.")
        
        # Welcome Email
        subject = "Welcome to Symptomate !!"
        message = "Hello " + user.first_name + "!! \n" + "Welcome to Symptomate!! \nThank you for visiting our website\nWe have also sent you a confirmation email, please confirm your email address. \n\nThanking You\n\nTeam Symptomate"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email SYMPTOMATE !!"
        message2 = f"Hello {user.first_name}! Welcome to Symptomate! Please click the following link to activate your account: \n\n{current_site.domain}/Authentication/activate/{urlsafe_base64_encode(force_bytes(user.pk))}/{generate_token.make_token(user)}"
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        email.send()
        
        return Response({'message': 'Account created successfully'}, status=status.HTTP_201_CREATED)

    def signin(self, request):
        username = request.data.get('username')
        pass1 = request.data.get('pass1')
        
        if not all([username, pass1]):
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            return Response({'message': 'Logged in successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = AuthUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, AuthUser.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return Response({'error': 'Activation failed'}, status=status.HTTP_400_BAD_REQUEST)

def signout(request):
    logout(request)
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)



class getAgeGender(Authentication):
    def post(self, request, *args, **kwargs):
        age = request.data.get('age')
        gender = request.data.get('gender')
        username = request.data.get('username')
        id  = request.data.get('id')
        try:
            user = AuthUser.objects.get(username=username)
        except AuthUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Create a serializer instance with data
        serializer = PostSerializer(data={'username': user.username, 'age': age, 'gender': gender,'id':id})

        # Check if data is valid and save it
        if serializer.is_valid():
            serializer.save()
            request.session['user_age'] = age
            request.session['user_gender'] = gender
            request.session['username'] = user.username  # Save the username instead of the user object
            request.session['id']=id
            return Response({'message': 'Age, gender, id and username stored successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class getMajorSymptoms(getAgeGender):
    def get(self, request, *args, **kwargs):
      age = request.session.get('user_age', 10)  # Default age to 10 if not provided
      gender = request.session.get('user_gender', 'Unknown')  # Default gender to Unknown if not provided
      if int(age) < 5:
        majorSymptoms = MajorSymptoms.objects.all().values('ms_name')
      else:
        majorSymptoms = MajorSymptomsAdult.objects.all().values('ms_name')
        
      list = [item['ms_name'] for item in majorSymptoms]
      return Response(list, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        age = request.session.get('user_age', 10)  # Default age to 10 if not provided
        gender = request.session.get('user_gender', 'Unknown')  # Default gender to Unknown if not provided
        if age is None:
            return Response({'error': 'Age parameter is missing'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            age = int(age)
        except ValueError:
            return Response({'error': 'Invalid age format'}, status=status.HTTP_400_BAD_REQUEST)
        if int(age) < 5:
            major_symptoms_model = MajorSymptoms.objects
            more_precise_symptoms_model = MorePreciseSymptoms.objects
        else:
            major_symptoms_model = MajorSymptomsAdult.objects
            more_precise_symptoms_model = MorePreciseSymptomsAdult.objects
        
        symptoms = request.data.get('symptoms', [])
        preSympList = []
        ms_ids = []
        for symptom in symptoms:
            symptom += "\r"
            try:
                ms1 = major_symptoms_model.get(ms_name__exact=symptom)
                serializer1 = MajorSympSerializer(ms1)
                ms_id = ms1.ms_id
                ms_ids.append(ms_id)
                precise = more_precise_symptoms_model.filter(link_1=ms_id)
                if int(age) <5:
                 serializer2 = MorePreSympSerializer(precise, many=True)
                else:
                 serializer2 = MorePreSympSerializerAdult(precise, many=True)
                preSympList.extend(item['mps_name'] for item in serializer2.data)
            except MajorSymptoms.DoesNotExist:
                return Response({'error': 'Major symptom not found'}, status=status.HTTP_404_NOT_FOUND)
        request.session['ms_ids'] = ms_ids
        return Response(preSympList, status=status.HTTP_200_OK)

class getPreciseSymptoms(getMajorSymptoms):
    def post(self, request, *args, **kwargs):
        age = request.session.get('user_age', 10)  # Default age to 10 if not provided
        gender = request.session.get('user_gender', 'Unknown')  # Default gender to Unknown if not provided
        # age = request.data.get('age', 10)  # Default age to 0 if not provided
        if int(age) < 5:
            precise_symptoms_model = MorePreciseSymptoms.objects
        else:
            precise_symptoms_model = MorePreciseSymptomsAdult.objects

        preSymps = request.data.get('preSymps', [])
        result = []
        mps_ids = []
        for preSymp in preSymps:
            try:
                mps = precise_symptoms_model.get(mps_name=preSymp)
                serializer = MorePreSympSerializer(mps)
                mps_id = mps.mps_id
                mps_ids.append(mps_id)
                result.append(serializer.data)
            except MorePreciseSymptoms.DoesNotExist:
                result.append({'error': f'Disease not found for {preSymp}'})
            except MorePreciseSymptoms.MultipleObjectsReturned:
                # If multiple objects are found, get the first one
                mps = precise_symptoms_model.filter(mps_name=preSymp).first()
                serializer = MorePreSympSerializer(mps)
                mps_id = mps.mps_id
                mps_ids.append(mps_id)
                result.append(serializer.data)
        request.session['mps_id'] = mps_ids
        return Response(result, status=status.HTTP_200_OK)


    def get(self, request, *args, **kwargs):
        age = request.session.get('user_age', 10)  # Default age to 10 if not provided
        gender = request.session.get('user_gender', 'Unknown')  # Default gender to Unknown if not provided
        # age = request.query_params.get('age', 10)  # Default age to 0 if not provided
        if int(age) < 5:
            precise_symptoms_model = MorePreciseSymptoms.objects
        else:
            precise_symptoms_model = MorePreciseSymptomsAdult.objects

        diseases = precise_symptoms_model.all()
        if int(age)<5:
            serializer = MorePreSympSerializer(diseases,many=True)
        else:
            serializer = MorePreSympSerializerAdult(diseases,many=True)  
        # serializer = MorePreSympSerializer(diseases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class getDiseases(getPreciseSymptoms):
    def post(self, request, *args, **kwargs):
        age = request.session.get('user_age', 10)  # Default age to 10 if not provided
        gender = request.session.get('user_gender', 'Unknown')  # Default gender to Unknown if not provided
        # username=request.session.get('username','Unknown')
        if int(age) < 5:
            diseases_model = Diseases.objects
        else:
            diseases_model = DiseasesAdult.objects
        
        mps_ids = request.session.get('mps_id')
        diseases = []

        for mps_id in mps_ids:
            disease_obj = diseases_model.filter(precise_symptom__exact=mps_id)
            for disease in disease_obj:
                disease_name = disease.d_name
                diseases.append(disease_name)

        # Join the list of diseases into a comma-separated string
        diseases_csv = ','.join(diseases)

        # Get the id of the corresponding PostsInfo object
        username_id = request.session.get('username')
        id=request.session.get('id')

        # Update the PostsInfo object with diseases
        try:
            posts_info = PostsInfo.objects.get(username=username_id,id=id)
            posts_info.disease = diseases_csv
            posts_info.save()
            return Response(diseases, status=status.HTTP_200_OK)
        except PostsInfo.DoesNotExist:
            return Response({'error': 'PostsInfo object does not exist'}, status=status.HTTP_404_NOT_FOUND)

class getPatientHistory(getDiseases):
    def get(self, request, *args, **kwargs):
        # Get the username from the session
        username = request.session.get('username')

        # Retrieve all PostsInfo objects for the current username
        posts_info_objects = PostsInfo.objects.filter(username=username)

        # Create a list to store patient history
        patient_history = []

        # Iterate over each PostsInfo object
        for posts_info in posts_info_objects:
            # Extract age, gender, and diseases from the PostsInfo object
            age = posts_info.age
            gender = posts_info.gender
            diseases = posts_info.disease.split(',')  # Assuming diseases are stored as comma-separated values

            # Create a dictionary to hold the information for this PostsInfo object
            data = {
                'age': age,
                'gender': gender,
                'diseases': diseases
            }

            # Append this dictionary to the patient history list
            patient_history.append(data)

        # Return the patient history list as a response
        return Response(patient_history, status=status.HTTP_200_OK)
