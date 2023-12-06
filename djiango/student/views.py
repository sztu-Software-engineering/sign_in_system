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
from django.db.models import Max
from collections import defaultdict
# Create your views here.
class studentSignup(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = studentSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            courseid=serializer.validated_data['courseid']
            state=serializer.validated_data['state']
            signinway=serializer.validated_data['signinway']
            user=request.user

            if Course.objects.filter(courseid=courseid).exists() and Student.objects.filter(studentid=user.username).exists() and state==1:
                eachcourseid = Signinmsg.objects.filter(courseid=courseid).aggregate(Max('eachcourseid'))['eachcourseid__max']
                print(eachcourseid)
                signInallTable=Signinmsg.objects.get(eachcourseid=eachcourseid)
                signInallTable.signinnum+=1
                signInallTable.save()
                Signmsg.objects.create(eachcourseid=eachcourseid,studentid=user.username,signinway=signinway)

                return Response({'status': ' success'})
        return Response({'status': ' fail'})
    def get(self, request):
        courseid = request.GET.get('courseid')
        if Signinmsg.objects.filter(courseid=courseid).exists():
            ##找到每节课的ID获取最新的签到码
            eachcourseid = Signinmsg.objects.filter(courseid=courseid).aggregate(Max('eachcourseid'))['eachcourseid__max']
            signInallTable = Signinmsg.objects.get(eachcourseid=eachcourseid)
            coursename=Course.objects.get(courseid=courseid).coursename
            return Response({'status': 'sucess','signIncode': signInallTable.signIncode,'beginTime': signInallTable.begintime,'coursename':coursename})
        return Response({'status': 'fail'})
"""给定courseid返回该学生的所有签到信息"""
class getStudentSignin(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        courseid = request.GET.get('courseid')
        studentId=request.user.username


