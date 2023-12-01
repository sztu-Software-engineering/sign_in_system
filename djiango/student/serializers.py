from django.contrib.auth.models import User
from rest_framework import serializers
from common.models import Student, Teacher,Course,Signmsg
from rest_framework.authtoken.models import Token
class studentSignupSerializer(serializers.Serializer):
    eachcourseid=serializers.CharField()
    signinway=serializers.CharField()
    state=serializers.IntegerField()
    def validated_eachcourseid(self, value):
        if not Signmsg.objects.filter(eachcourseid=value).exists():
            raise serializers.ValidationError("Course with this courseid does not exist")
        return value
    def validated_state(self, value):
        if value!=0 || value!=1:
            raise serializers.ValidationError("state must be 0 or 1")
        return value
