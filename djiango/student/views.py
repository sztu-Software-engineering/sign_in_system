from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login

from django.contrib.auth.models import User
# Create your views here.
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common.models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from common.models import *
# Create your views here.
class studentSignup(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = studentSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            eachcourseid=serializer.validated_data['courseid']
            state=serializer.validated_data['state']
            signinway=serializer.validated_data['signinway']
            user=request.user
            if Student.objects.filter(studentid=user.username).exists() and Signinmsg.objects.filter(eachcourseid=eachcourseid).exists() and state==1:
                signInallTable=Signinmsg.objects.get(eachcourseid=eachcourseid)
                signInallTable.signinnum+=1
                signInallTable.save()
                Signmsg.objects.create(eachcourseid=eachcourseid,studentid=user.username,signinway=signinway)

                return Response({'status': ' success'})
        return Response({'status': ' fail'})