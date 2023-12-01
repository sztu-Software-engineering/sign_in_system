import requests
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
    url = "http://127.0.0.1:8000/login/"
    response = requests.post(url, json={
        "Authentication": 1,
        "password": "1",
        "username": "fuck",
        "usernumber": "1"
    })
    print(response.status_code)
    print(response.json())  # If you expect a JSON response
def testLogout():
    url = 'http://127.0.0.1:8000/logout/'
    token = 'c84d3f192585dc1979ae4725418bb750a5e7831c'

    headers = {
        'Authorization': f'Token {token}',
    }

    response = requests.post(url, headers=headers)

    print(response.status_code)
    print(response.json())
testLogout()