from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login
from .models import *
from .serializers import *
from django.contrib.auth.models import User
# Create your views here.
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .models import Teacher
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from silk.profiling.profiler import silk_profile
class RegistrationView(APIView):
    @silk_profile()
    def post(self, request):
        authentication_type = request.data.get('Authentication')
        serializer = RegistrationSerializer(data=request.data)
        if User.objects.filter(username=request.data.get('usernumber')).exists():

            return Response({'status': 'exist'})
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success'})
        return Response({'status': 'fail'})
class LoginView(APIView):
    @silk_profile()
    def post(self, request):

        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            if user:
                # login(request,user)
                token, created = Token.objects.get_or_create(user=user)

                if Student.objects.filter(studentid=user.username).exists():
                    student=Student.objects.get(studentid=user.username)
                    return Response({'status': 'success','token':token.key,"class_field":student.class_field,"academy":student.colleage})
                else:
                    teacher=Teacher.objects.get(teachernum=user.username)
                    return Response({'status': 'success','token':token.key,"academy":teacher.colleage})

        return Response({'status': 'fail'})

class ChooseCourseListView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @silk_profile()
    def get(self,request):
        user=request.user

        if Student.objects.filter(studentid=user.username).exists():
            student=Student.objects.get(studentid=user.username)
            chosen_courses = student.chosen_courses.all()
            course_ids = [course.courseid.courseid for course in chosen_courses]
            courses = Course.objects.filter(courseid__in=course_ids)

            serializer = CourseListSerializer(courses, many=True)
            # print(serializer.data)

            # print(student.name)
            # print(serializer.data)
            return Response(serializer.data)
        if Teacher.objects.filter(teachernum=user.username).exists():
            teacher=Teacher.objects.get(teachernum=user.username)
            print(teacher.teachername)
            courses_taught_by_teacher = Course.objects.filter(teachernum=user.username)
            serializer = CourseListSerializer(courses_taught_by_teacher, many=True)
            print(serializer.data)
            return Response(serializer.data)

        print(user)

        return Response({'status': 'success'})
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @silk_profile()
    def post(self, request):
        # Delete the user's token to log them out
        request.user.is_active = False
        request.user.save()
        request.auth.delete()
        return Response({'status': 'success'})
class addCourse(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @silk_profile()
    def post(self, request):
        # print(request.headers)
        courseid=request.data.get('classnumber')

        user=request.user
        if Student.objects.filter(studentid=user.username).exists():
            if not Course.objects.filter(courseid=courseid).exists():
                return Response({'status': 'fail', 'message': '课程不存在'})
            if Choosecoursemsg.objects.filter(courseid=courseid,studentid=user.username).exists():
                return Response({'status': 'exist', 'message': '已经选择过该课程'})

            studentCourse=Choosecoursemsg.objects.create(courseid=Course.objects.get(courseid=courseid),studentid=Student.objects.get(studentid=user.username))
            course=Course.objects.get(courseid=courseid)
            course.choosenum+=1
            course.save()
            studentCourse.save()
            # print(studentCourse)
            return Response({'status': 'success','message':'加入成功'})
        elif Teacher.objects.filter(teachernum=user.username).exists():
            if Course.objects.filter(courseid=courseid).exists():
                return Response({'status': 'exist', 'message': '课程号已存在'})
            coursename=request.data.get('classname')
            # print(user.username)
            teacherCourse=Course.objects.create(courseid=courseid,teachernum=Teacher.objects.get(teachernum=user.username),choosenum=0,courseName=coursename)
            teacherCourse.save()
            # print(teacherCourse)
            return Response({'status': 'success','message':'开设成功'})

        return Response({'status': 'fail'})
class getCourseList(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @silk_profile()
    def get(self,request):
        # print(request.headers)
        username=request.user.username
        if Student.objects.filter(studentid=username).exists():
            chosen_courses = Choosecoursemsg.objects.filter(studentid=username)
            # print(username)
            course_ids = [chosen_course.courseid.courseid for chosen_course in chosen_courses]
            print(course_ids)
            chosen_coursesName=Course.objects.filter(courseid__in=course_ids)
            # print(chosen_coursesName)
            courseLists=[]
            courseList={}

            for course in chosen_coursesName:
                # print(course.courseName)
                courseList={"classname": course.courseName,"classnumber": course.courseid}
                courseLists.append(courseList)

            return Response(courseLists)
        elif Teacher.objects.filter(teachernum=username).exists():
            teacher=Teacher.objects.get(teachernum=username)
            courses_taught_by_teacher = Course.objects.filter(teachernum=username)
            courseLists=[]
            courseList={}
            for course in courses_taught_by_teacher:
                courseList={"classname": course.courseName,"classnumber": course.courseid}
                courseLists.append(courseList)
            return Response(courseLists)

