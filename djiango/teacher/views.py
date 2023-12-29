from django.shortcuts import render
from django.http import HttpResponse
from common.models import *
from teacher.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import random
from datetime import datetime
from datetime import datetime, timezone
from django.db.models import Max
from django.db.models import F
from django.http import FileResponse
import qrcode
import io
"""
    教师发起签到
    返回值：satus:success/fail，签到码：signincode
"""
class teacherRegisterEachCourse(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            courseid = request.GET.get('classnumber')
            try:
                limitTime = request.GET.get('limittime')
            except:
                limitTime = 99999
        except:
            return Response({'status': 'fail'})

        if Course.objects.filter(courseid=courseid).exists():
            record_count = Signinmsg.objects.filter(courseid=courseid).count()
            if(Signinmsg.objects.filter(eachcourseid=(courseid+str(record_count).zfill(3))).exists()):
                checkIfOverTime = Signinmsg.objects.get(eachcourseid=(courseid+str(record_count).zfill(3)))
                now = datetime.now(timezone.utc)
                if (now - checkIfOverTime.begintime).seconds < checkIfOverTime.limitTime:


                    return Response({'status': 'success', 'code': checkIfOverTime.signIncode})


            each = str(record_count + 1).zfill(3)
            print(courseid + each)
            signin_code = random.randint(100000, 999999)
            eachcourse_id = courseid + each
            current_time = datetime.now()
            Signinmsg.objects.create(courseid=Course.objects.get(courseid=courseid), eachcourseid=eachcourse_id, signinnum=0, begintime=current_time,signIncode=signin_code,limitTime=limitTime)
            # 所有一选这节课的学生全部标记为未签到
            Choosecourses = Choosecoursemsg.objects.filter(courseid=courseid)
            for choosecourse in Choosecourses:
                Signmsg.objects.create(eachcourseid=Signinmsg.objects.get(eachcourseid=eachcourse_id), studentid=choosecourse.studentid, signinway=0)

            return Response({'status': 'success', 'code': signin_code})
        return Response({'status': 'fail'})
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
class GetAllSigninData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        courseid=request.GET.get('classnumber')
        if Signinmsg.objects.filter(courseid=courseid).exists():
            ##get all the signinmsg of this course
            signmsgs = Signinmsg.objects.filter(courseid=courseid)
           ##return time ,checkin number ,uncheckin number
            data = [{
                'time': signmsg.begintime.strftime("%Y.%m.%d %H:%M:%S"),
                'checkinNumber': signmsg.signinnum,
                'uncheckinNumber': Course.objects.get(courseid=courseid).choosenum - signmsg.signinnum
            } for signmsg in signmsgs]
            return Response(data)
        return Response({'status': 'fail'})

# Create your views here.
class getSignInNumber(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        courseid=request.GET.get('classnumber')
        if Signinmsg.objects.filter(courseid=courseid).exists():
            ##找到每节课的ID获取最新的签到码
            eachcourseid = Signinmsg.objects.filter(courseid=courseid).aggregate(Max('eachcourseid'))['eachcourseid__max']
            try:

                signInallTable=Signinmsg.objects.get(eachcourseid=eachcourseid)
                # get the number of students who have choosen this course
                course = Course.objects.get(courseid=courseid)
                return Response({'status': 'sucess', 'checkinNumber': signInallTable.signinnum,
                                 "uncheckinNumber": course.choosenum - signInallTable.signinnum})
            except:
                return Response({'status': 'fail'})

        return Response({'status': 'fail'})

class getQRCode(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            courseid = request.GET.get('classnumber')
            try:
                limitTime = request.GET.get('limittime')
            except:
                limitTime = 99999
        except:
            return Response({'status': 'fail'})

        if Course.objects.filter(courseid=courseid).exists():
            record_count = Signinmsg.objects.filter(courseid=courseid).count()
            if(Signinmsg.objects.filter(eachcourseid=(courseid+str(record_count).zfill(3))).exists()):
                checkIfOverTime = Signinmsg.objects.get(eachcourseid=(courseid+str(record_count).zfill(3)))
                now = datetime.now(timezone.utc)
                if (now - checkIfOverTime.begintime).seconds < checkIfOverTime.limitTime:

                    img = qrcode.make(checkIfOverTime.signIncode)  # 传入网址计算出二维码图片字节数据
                    buf = io.BytesIO()  # 创建一个BytesIO临时保存生成图片数据
                    img.save(buf)  # 将图片字节数据放到BytesIO临时保存
                    image_stream = buf.getvalue()  # 在BytesIO临时保存拿出数据

                    response = HttpResponse(image_stream, content_type="image/jpg")
                    return response

            each = str(record_count + 1).zfill(3)
            print(courseid + each)
            signin_code = random.randint(100000, 999999)
            eachcourse_id = courseid + each
            current_time = datetime.now()
            Signinmsg.objects.create(courseid=Course.objects.get(courseid=courseid), eachcourseid=eachcourse_id, signinnum=0, begintime=current_time,signIncode=signin_code,limitTime=limitTime)
            # 所有一选这节课的学生全部标记为未签到
            Choosecourses = Choosecoursemsg.objects.filter(courseid=courseid)
            for choosecourse in Choosecourses:
                Signmsg.objects.create(eachcourseid=Signinmsg.objects.get(eachcourseid=eachcourse_id), studentid=choosecourse.studentid, signinway=0)

            signin_code_str = str(signin_code)
            print(signin_code_str)
            img = qrcode.make(signin_code_str)  # 传入网址计算出二维码图片字节数据
            buf = io.BytesIO()  # 创建一个BytesIO临时保存生成图片数据
            img.save(buf)  # 将图片字节数据放到BytesIO临时保存
            image_stream = buf.getvalue()  # 在BytesIO临时保存拿出数据

            response = HttpResponse(image_stream, content_type="image/jpg")  # 将二维码数据返回到页面
            return response

        return Response({'status': 'fail'})
