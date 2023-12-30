from datetime import datetime, timezone

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
from django.db.models import F
from silk.profiling.profiler import silk_profile
from collections import defaultdict
# Create your views here.
#学生签到
class studentSignup(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @silk_profile()
    def post(self, request):
        print(request.data)
        serializer = studentSignupSerializer(data=request.data)

        if serializer.is_valid():
            courseid=serializer.validated_data['classnumber']
            code=serializer.validated_data['code']
            user=request.user

            if Course.objects.filter(courseid=courseid).exists() and Student.objects.filter(studentid=user.username).exists() :
                eachcourseid = Signinmsg.objects.filter(courseid=courseid).aggregate(Max('eachcourseid'))['eachcourseid__max']
                print(eachcourseid)
                signInallTable=Signinmsg.objects.get(eachcourseid=eachcourseid)
                if(Signmsg.objects.get(eachcourseid=eachcourseid,studentid=user.username).signinway!='0'):
                    # print(Signmsg.objects.get(eachcourseid=eachcourseid,studentid=user.username).signinway)
                    return Response({'status': 'fail','message':'已经签到过了'})
                now = datetime.now(timezone.utc)
                # print((now - signInallTable.begintime).seconds)
                if (now - signInallTable.begintime).seconds > signInallTable.limitTime:
                    return Response({'status': 'fail','message':'签到超时'})
                if signInallTable.signIncode!=code:
                    return Response({'status': 'fail','message':'签到码错误'})
                signInallTable.signinnum+=1
                signInallTable.save()
                ChangeSignmsg=Signmsg.objects.get(eachcourseid=eachcourseid,studentid=user.username)
                ChangeSignmsg.signinway=1
                ChangeSignmsg.save()
                return Response({'status': 'success','message':'签到成功'})
        return Response({'status': 'fail'})
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

    @silk_profile()
    def get(self, request):
        coursename = request.GET.get('classname')
        studentId=request.user.username
        if Course.objects.filter(courseName=coursename).exists():
            courseid=Course.objects.get(courseName=coursename).courseid
            if Signmsg.objects.filter(eachcourseid__courseid=courseid,studentid=studentId).exists():
                signmsgs = Signmsg.objects.filter(eachcourseid__courseid=courseid,studentid=studentId).annotate(
                    courseid=F('eachcourseid__courseid'),
                    begintime=F('eachcourseid__begintime')
                )

                data = [StudentSignInInfoSerializer({
                    'time': signmsg.begintime.strftime("%Y.%m.%d %H:%M:%S"),
                    'state': signmsg.signinway,
                }).data for signmsg in signmsgs]
                return Response(data)
            else:
                return Response({'status': 'fail'})

        return Response({'status': 'fail'})



