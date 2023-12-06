# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Choosecoursemsg(models.Model):
    courseid = models.OneToOneField('Course', models.DO_NOTHING, db_column='CourseID', primary_key=True)  # Field name made lowercase.
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='StudentID',related_name='chosen_courses')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChooseCourseMsg'
        unique_together = (('courseid', 'studentid'),)


class Course(models.Model):
    courseid = models.CharField(db_column='CourseID', primary_key=True, max_length=10)  # Field name made lowercase.
    teachernum = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='TeacherNum')  # Field name made lowercase.
    choosenum = models.IntegerField(db_column='ChooseNum')  # Field name made lowercase.
    courseName=models.CharField(db_column='CourseName',max_length=20)
    class Meta:
        managed = True
        db_table = 'Course'


class Signmsg(models.Model):
    id=models.AutoField(primary_key=True)
    eachcourseid = models.ForeignKey('Signinmsg', models.DO_NOTHING, db_column='EachCourseID',primary_key=False)  # Field name made lowercase.
    studentid = models.OneToOneField('Student', models.DO_NOTHING, db_column='StudentID')  # Field name made lowercase.
    signinway = models.CharField(db_column='SignInWay', max_length=10)  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'SignMsg'


class Student(models.Model):
    studentid = models.CharField(db_column='StudentID', primary_key=True, max_length=15)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=10)  # Field name made lowercase.
    colleage = models.CharField(db_column='Colleage', max_length=10)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=10)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        managed = True
        db_table = 'Student'


class Teacher(models.Model):
    teachernum = models.CharField(db_column='TeacherNum', primary_key=True, max_length=15)  # Field name made lowercase.
    teachername = models.CharField(db_column='TeacherName', max_length=15)  # Field name made lowercase.
    colleage = models.CharField(db_column='Colleage', max_length=10)  # Field name made lowercase.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        managed = True
        db_table = 'Teacher'


class Signinmsg(models.Model):
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='CourseID')  # Field name made lowercase.
    eachcourseid = models.CharField(db_column='EachCourseID', primary_key=True, max_length=10)  # Field name made lowercase.
    signinnum = models.IntegerField(db_column='SignInNum')  # Field name made lowercase.
    begintime = models.DateField(db_column='BeginTime', blank=True, null=True)  # Field name made lowercase.
    signIncode=models.CharField(db_column='SignInCode',max_length=5)

    class Meta:
        managed = True
        db_table = 'signInMsg'
