import requests
# from common.models import *
def testGetCourse():
    url = 'http://127.0.0.1:8000/chooseCourseList/'
    token = 'c84d3f192585dc1979ae4725418bb750a5e7831c'

    headers = {
        'Authorization': f'Token {token}',
    }

    response = requests.get(url, headers=headers)

    print(response.status_code)
    print(response.json())  # If you expect a JSON response
def testLogin():
    url = "http://47.120.52.230:8000/login"
    response = requests.post(url, json={
        "Authentication": 1,
        "password": "1111",
        "username": "123431",
        "usernumber": "123431"
    })
    print(response.status_code)
    print(response.headers)
    print(response.json())# If you expect a JSON response
def testLogout():
    url = 'http://127.0.0.1:8000/logout/'
    token = 'c84d3f192585dc1979ae4725418bb750a5e7831c'

    headers = {
        'Authorization': f'Token {token}',
    }

    response = requests.post(url, headers=headers)

    print(response.status_code)
    print(response.json())



# signmsgs = Signmsg.objects.all().annotate(
#     courseid=F('eachcourseid__courseid'),
#     begintime=F('eachcourseid__begintime')
# )
# #
# #
# for signmsg in signmsgs:
#     print(signmsg.courseid, signmsg.begintime)
def testRegister():
    url='http://47.120.52.230:8000/register'
    response = requests.post(url, json={
        "Authentication": 0,
        "password": "1111",
        "username": "fffff",
        "usernumber": "123431",
        "class_field": "1",
        "academy": "bdi"
    })
    print(response.status_code)
    print(response.json())
def getStudentSignInInfo():
    url = 'http://127.0.0.1:8000/student/getStudentSignin/'
    token='c2b914c6f833114fc5bcb1924f3cd018833b45a9'
    courseid='000001'
    headers = {
        'Authorization': f'Token {token}',
    }
    params = {
        'courseid': courseid,
    }
    response = requests.get(url, headers=headers,params=params)
    print(response.status_code)
    print(response.json())
testLogin()