from django.shortcuts import render
from django.http import HttpResponse
from common.models import *
from serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class teacherRegisterEachCourse(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = teacherRegisterEachCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': ' success'})
        return Response({'status': ' fail'})
# Create your views here.
