from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

class StudentRegistrationTest(TestCase):
    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username='1111', password='1111')


    def test_create_student_user(self):
        client = APIClient()

        # Login to get the authentication token
        client.login(username='testuser', password='testpassword')

        # Define the data for creating a student user
        student_data = {
            "Authentication": 0,  # Assuming 0 represents a student
            "usernumber": "student123",
            "password": "studentpassword",
            "username": "studentusername",
            "class_field": "class123",
            "colleage": "engineering",
        }

        # Make a POST request to create a student user
        response = client.post('/your_registration_endpoint/', data=student_data, format='json')

        # Check if the response status is HTTP_201_CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the student user is created in the database
        self.assertTrue(User.objects.filter(username='student123').exists())

        # Optionally, you can check other details in the response or perform additional assertions
        # For example, you might want to check if the returned JSON contains the expected data.

    def tearDown(self):
        # Clean up after the test
        self.user.delete()
.login(username='test@dom.com', password='pass')