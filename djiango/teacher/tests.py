from django.test import TestCase
import requests
# Create your tests here.
def testLogin():
    url = "http://127.0.0.1:8000/login/"
    response = requests.post(url, json={
        "Authentication": 1,
        "password": "1",
        "username": "h",
        "usernumber": "1234"
    })
    print(response.status_code)
    print(response.json())# If you expect a JSON response
def testGetsignIndata():
    loginurl = "http://127.0.0.1:8000/login/"
    response = requests.post(loginurl, json={
        "Authentication": 1,
        "password": "1",
        "username": "h",
        "usernumber": "1234"
    })
    url = 'http://127.0.0.1:8000/teacher/teacherGetSigninData'
    token = response.headers
    print(token)
    headers = {
        'Authorization': f'Token {token}',
    }

    response = requests.get(url, headers=headers,params='000001001')
    print(response.status_code)
    print(response.json())  # If you expect a JSON response
testGetsignIndata()