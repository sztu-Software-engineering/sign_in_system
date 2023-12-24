from django.contrib.auth.models import User
from rest_framework import serializers
from common.models import Student, Teacher,Course,Signmsg
from rest_framework.authtoken.models import Token
class studentSignupSerializer(serializers.Serializer):
    classnumber=serializers.CharField()
    code=serializers.CharField()
class StudentSignInInfoSerializer(serializers.Serializer):
    time = serializers.DateTimeField()
    state = serializers.IntegerField()