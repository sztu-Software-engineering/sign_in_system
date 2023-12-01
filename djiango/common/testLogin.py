import requests


url = "http://127.0.0.1:8000/login/"


# headers = {
#     'Authorization': f'Token {token}',
# }

response = requests.post(url, json={
            "Authentication": 1,
            "password": "1",
            "username": "fuck",
            "usernumber": "1"
        })

print(response.status_code)
print(response.json())  # If you expect a JSON response
