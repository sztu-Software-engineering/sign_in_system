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
        "Authentication": 0,
        "password": "1111",
        "username": "hsk",
        "usernumber": "202200202000"
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
        "username": "xjp",
        "usernumber": "202200202002",
        "course": "1",
        "academy": "bdi"
    })
    print(response.status_code)
    print(response.json())
def getStudentSignInInfo():
    url = 'http://127.0.0.1:8000/student/getStudentSignin/'
    token='8f643bf7faaf513577f36fdeb321bc4697659d58'
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
def testTeacherAddCourse():
    url = 'http://47.120.52.230:8000/addCourse'
    token ='0af07b4721908ffc01c0478f30878fe700d4d231'
    headers = {
        'Authorization': f'Token {token}',
    }
    print(headers)
    response = requests.post(url, headers=headers,json={
        "classnumber": "000001",
        "classname": "数据结构",
    })
    print(response.json())
def testStudentAddCourse():
    url = 'http://47.120.52.230:8000/addCourse'
    token ='7def3176351267f6ff4564792233a04606a2523c'
    headers = {
        'Authorization': f'Token {token}',
    }
    response = requests.post(url, headers=headers,json={
        "classnumber": "000005",
    })
    print(response.json())
def testGetCourse():
    url = 'http://47.120.52.230:8000/getCourseList'
    token = 'd07b14c46f80949466e389b6e818d95818b592e3'
    headers = {
        'Authorization': f'Token {token}',
    }

    response = requests.get(url, headers=headers)
    print(response.json())
def Registerbaolitest():
    url='http://47.120.52.230:8000/register'
    response = requests.post(url, json={
        "Authentication": 0,
        "password": "1111",
        "username": "xjp",
        "usernumber": "202200202002",
        "course": "1",
        "academy": "bdi"
    })
    print(response.status_code)
    print(response.json())
testLogin()

