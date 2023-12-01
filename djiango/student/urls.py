from django.urls import path

from . import views
app_name = "student"
urlpatterns = [
    path('studentSignUpRrecord/', views.studentSignup.as_view(), name='studentSignUpRrecord'),
]