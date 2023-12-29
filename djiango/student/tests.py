from django.test import TestCase
import requests
def testStudentSignIn():
    url = 'http://47.120.52.230:8000/student/studentSignUpRrecord'
    token ='7def3176351267f6ff4564792233a04606a2523c'
    headers = {
        'Authorization': f'Token {token}',
    }
    response = requests.post(url, headers=headers,json={
        "classnumber": "000001",
        "code":"450390"
    })
    print(response.json())
# Create your tests here.
def testGetStudentSigninMsg():
    url='http://47.120.52.230:8000/student/getStudentSignin'
    token = '7def3176351267f6ff4564792233a04606a2523c'
    headers = {
        'Authorization': f'Token {token}',
    }

    respone=requests.get(url,headers=headers,params={
        "classname":"数据结构"
    })
    print(respone.json())
testGetStudentSigninMsg()