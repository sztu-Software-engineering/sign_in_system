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

class RegistrationView(APIView):
    def post(self, request):
        authentication_type = request.data.get('Authentication')
        print(request.data)
        serializer = RegistrationSerializer(data=request.data)
        if User.objects.filter(username=request.data.get('usernumber')).exists():
            print("exist")
            return Response({'status': ' exist'})
        if serializer.is_valid():
            serializer.save()
            return Response({'status': ' success'})
        return Response({'status': ' fail'})
class LoginView(APIView):
    def post(self, request):

        serializer=LoginSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            user=serializer.save()
            if user:
                # login(request,user)
                token, created = Token.objects.get_or_create(user=user)
                print(token.key)
                return Response({'status': ' success','token':token.key})
        return Response({'status': ' fail'})

class ChooseCourseListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user=request.user

        if Student.objects.filter(studentid=user.username).exists():
            student=Student.objects.get(studentid=user.username)
            chosen_courses = student.chosen_courses.all()
            course_ids = [course.courseid.courseid for course in chosen_courses]
            courses = Course.objects.filter(courseid__in=course_ids)

            serializer = CourseListSerializer(courses, many=True)
            print(serializer.data)

            print(student.name)
            print(serializer.data)
            return Response(serializer.data)
        if Teacher.objects.filter(teachernum=user.username).exists():
            teacher=Teacher.objects.get(teachernum=user.username)
            print(teacher.teachername)
            courses_taught_by_teacher = Course.objects.filter(teachernum=user.username)
            serializer = CourseListSerializer(courses_taught_by_teacher, many=True)
            print(serializer.data)
            return Response(serializer.data)

        print(user)

        return Response({'status': ' success'})
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # Delete the user's token to log them out
        request.user.is_active = False
        request.user.save()
        request.auth.delete()
        return Response({'status': 'success'})
