from rest_framework import serializers
from . import *
# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Student, Teacher,Course
from rest_framework.authtoken.models import Token
class RegistrationSerializer(serializers.Serializer):
    Authentication=serializers.IntegerField()
    class_field=serializers.CharField()
    password=serializers.CharField()
    username=serializers.CharField()
    usernumber=serializers.CharField()
    academy=serializers.CharField()
    def validate_usernumber(self, value):
        # 在这里检查 usernumber 是否在 User 模型中存在
        if User.objects.filter(username=value).exists():

            raise serializers.ValidationError("User with this usernumber does not exist")
        return value
    def create(self, validated_data):
        Authentication=validated_data['Authentication']
        class_field=validated_data['class_field']
        password=validated_data['password']
        username=validated_data['username']
        usernumber=validated_data['usernumber']
        academy=validated_data['academy']
        user=User.objects.create(username=usernumber,password=password)
        if Authentication==0:
            student=Student.objects.create(user=user,class_field=class_field,studentid=usernumber,name=username,colleage=academy)
            return student
        else:
            teacher=Teacher.objects.create(user=user,teachernum=usernumber,teachername=username,colleage=academy)
            return teacher
class LoginSerializer(serializers.Serializer):
    Authentication=serializers.IntegerField()
    usernumber=serializers.CharField()
    password = serializers.CharField()
    username=serializers.CharField()
    def validate_usernumber(self, value):
        # 在这里检查 usernumber 是否在 User 模型中存在
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError("User with this usernumber does not exist")
        return value
    def validate_password(self, value):
        usernumber = self.initial_data.get('usernumber')
        # 在这里执行验证逻辑，例如检查密码是否正确
        try:
            user = User.objects.get(username=usernumber)
            if user.password == value:
                return value
            else:
                print(111)
                raise serializers.ValidationError("Incorrect password")
        except User.DoesNotExist:
            print(222)
            raise serializers.ValidationError("User does not exist")

    def create(self, validated_data):
        Authentication=validated_data['Authentication']
        password=validated_data['password']
        usernumber=validated_data['usernumber']
        username=validated_data['username']

        user=User.objects.get(username=usernumber)
        if user.password==password:
            user.is_active=True
            user.save()
            return user
        else:
            return serializers.ValidationError("Incorrect password")

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['courseName', 'courseid']



