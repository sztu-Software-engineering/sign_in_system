from django.urls import path

from . import views
app_name = "teacher"
urlpatterns = [
    path('teacherRegisterEachCourse', views.teacherRegisterEachCourse.as_view(), name='teacherRegisterEachCourse'),
    path('teacherGetSigninData', views.teacherGetSigninData.as_view(), name='teacherGetSigninData'),

]