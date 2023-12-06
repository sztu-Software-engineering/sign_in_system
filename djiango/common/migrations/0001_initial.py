# Generated by Django 4.1 on 2023-12-06 03:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseid', models.CharField(db_column='CourseID', max_length=10, primary_key=True, serialize=False)),
                ('choosenum', models.IntegerField(db_column='ChooseNum')),
                ('courseName', models.CharField(db_column='CourseName', max_length=20)),
            ],
            options={
                'db_table': 'Course',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Signinmsg',
            fields=[
                ('eachcourseid', models.CharField(db_column='EachCourseID', max_length=10, primary_key=True, serialize=False)),
                ('signinnum', models.IntegerField(db_column='SignInNum')),
                ('begintime', models.DateField(blank=True, db_column='BeginTime', null=True)),
                ('signIncode', models.CharField(db_column='SignInCode', max_length=5)),
                ('courseid', models.ForeignKey(db_column='CourseID', on_delete=django.db.models.deletion.DO_NOTHING, to='common.course')),
            ],
            options={
                'db_table': 'signInMsg',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Choosecoursemsg',
            fields=[
                ('courseid', models.OneToOneField(db_column='CourseID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='common.course')),
            ],
            options={
                'db_table': 'ChooseCourseMsg',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teachernum', models.CharField(db_column='TeacherNum', max_length=15, primary_key=True, serialize=False)),
                ('teachername', models.CharField(db_column='TeacherName', max_length=15)),
                ('colleage', models.CharField(db_column='Colleage', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Teacher',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentid', models.CharField(db_column='StudentID', max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=10)),
                ('colleage', models.CharField(db_column='Colleage', max_length=10)),
                ('class_field', models.CharField(db_column='Class', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Student',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Signmsg',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('signinway', models.CharField(db_column='SignInWay', max_length=10)),
                ('eachcourseid', models.ForeignKey(db_column='EachCourseID', on_delete=django.db.models.deletion.DO_NOTHING, to='common.signinmsg')),
                ('studentid', models.OneToOneField(db_column='StudentID', on_delete=django.db.models.deletion.DO_NOTHING, to='common.student')),
            ],
            options={
                'db_table': 'SignMsg',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='course',
            name='teachernum',
            field=models.ForeignKey(db_column='TeacherNum', on_delete=django.db.models.deletion.DO_NOTHING, to='common.teacher'),
        ),
    ]
