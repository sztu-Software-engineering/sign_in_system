from django.urls import path

from . import views
app_name = "teacher"
urlpatterns = [
    path('teacherRegisterEachCourse', views.teacherRegisterEachCourse.as_view(), name='teacherRegisterEachCourse'),
    path('getAllSigninData', views.GetAllSigninData.as_view(), name='teacherGetSigninData'),
    path('getSignInNumber', views.getSignInNumber.as_view(), name='getSignInNumber'),
    path('getQRcode', views.getQRCode.as_view(), name='getQRcode'),
]