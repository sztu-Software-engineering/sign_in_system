from django.test import TestCase
import requests
from PIL import Image
import io
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
def testbeginSignin():
    url = 'http://47.120.52.230:8000/teacher/teacherRegisterEachCourse'
    token = '8f643bf7faaf513577f36fdeb321bc4697659d58'
    headers = {
        'Authorization': f'Token {token}',
    }
    response = requests.get(url, headers=headers, params={
        "classnumber": "000001",
        "limittime": "60",
    })
    print(response.json())
def testGetSigninMsg():
    url = 'http://47.120.52.230:8000/teacher/getSignInNumber'
    token = '8f643bf7faaf513577f36fdeb321bc4697659d58'
    headers = {
        'Authorization': f'Token {token}',
    }
    response = requests.get(url, headers=headers, params={
        "classnumber": "000001",
    })
    print(response.json())
def testGetAllSignInmsg():
    url = 'http://47.120.52.230:8000/teacher/getAllSigninData'
    token = '8f643bf7faaf513577f36fdeb321bc4697659d58'
    headers = {
        'Authorization': f'Token {token}',
    }
    response = requests.get(url, headers=headers, params={
        "classnumber": "000001",
    })
    print(response.json())
def testGetQRinMsg():
    url = 'http://47.120.52.230:8000/teacher/getQRcode'
    token = '8f643bf7faaf513577f36fdeb321bc4697659d58'
    headers = {
        'Authorization': f'Token {token}',
    }
    response = requests.get(url, headers=headers, params={
        "classnumber": "000001",
        "limittime": "60",
    })

    # Check if the response headers indicate an image
    if 'image' in response.headers['Content-Type']:
        # Try to display the image
        try:
            image_bytes = io.BytesIO(response.content)
            img = Image.open(image_bytes)
            img.show()
        except PIL.UnidentifiedImageError:
            print("The server response is not a valid image.")
    else:
        print("The server response is not an image.")
testGetQRinMsg()