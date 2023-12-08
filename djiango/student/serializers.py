from django.contrib.auth.models import User
from rest_framework import serializers
from common.models import Student, Teacher,Course,Signmsg
from rest_framework.authtoken.models import Token
class studentSignupSerializer(serializers.Serializer):
    courseid=serializers.CharField()
    signinway=serializers.CharField()
    state=serializers.IntegerField()
    def validated_state(self, value):
        if (value!=0 or value!=1):
            raise serializers.ValidationError("state must be 0 or 1")
        return value

class StudentSignInInfoSerializer(serializers.Serializer):
    time = serializers.DateTimeField()
    state = serializers.IntegerField()