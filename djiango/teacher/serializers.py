from django.contrib.auth.models import User
from rest_framework import serializers
from common.models import Student, Teacher,Course,Signmsg
from rest_framework.authtoken.models import Token
class teacherRegisterEachCourseSerializer(serializers.Serializer):
    classnumber=serializers.CharField()
    limitTime=serializers.IntegerField()
    def validated_courseid(self, value):
        if not Course.objects.filter(courseid=value).exists():
            raise serializers.ValidationError("Course with this courseid do not exists")
        return value
