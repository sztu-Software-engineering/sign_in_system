from django.shortcuts import render
from django.http import HttpResponse
from common.models import *
from serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import random
"""
    教师发起签到
    返回值：satus:success/fail，签到码：signincode
"""
class teacherRegisterEachCourse(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = teacherRegisterEachCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            courseid=serializer.validated_data['courseid']
            beginTime=serializer.validated_data['beginTime']
            teacherid=request.user.username
            if Teacher.objects.filter(teachernum=teacherid).exists() and Course.objects.filter(courseid=courseid).exists():
                record_count = Signinmsg.objects.filter(courseid=courseid).count()
                each=str(record_count+1).zfill(3)
                print(courseid+each)
                signin_code = random.randint(1000, 9999)
                eachcourse_id=courseid+each
                Signinmsg.objects.create(courseid=courseid,eachcourseid=eachcourse_id,signinnum=0,begintime=beginTime,signIncode=signin_code)
                return Response({'status': ' success','signincode':signin_code,'eachcourseid':eachcourse_id})
            return Response({'status': ' fail'})
        return Response({'status': ' fail'})


# Create your views here.
