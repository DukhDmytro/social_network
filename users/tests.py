from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class RegistrationTestCase(APITestCase):
    def test_registration(self):
        # registration of user
        data = {'username': 'test_user', 'email': 'test@gmail.com', 'password': '12345'}
        response = self.client.post('http://127.0.0.1:8000/signup', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # registration of existing user
        data = {'username': 'test_user', 'email': 'test@gmail.com', 'password': '12345'}
        response = self.client.post('http://127.0.0.1:8000/signup', data)

    def test_invalid_registration(self):
        # registration without password
        data = {'username': 'test_user', 'email': 'test@gmail.com', 'password': ''}
        response = self.client.post('http://127.0.0.1:8000/signup', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # registration without username
        data = {'username': '', 'email': 'test@gmail.com', 'password': '12345'}
        response = self.client.post('http://127.0.0.1:8000/signup', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login(self):
        # registration of user
        data = {'username': 'test_user', 'email': 'test@gmail.com', 'password': '12345'}
        response = self.client.post('http://127.0.0.1:8000/signup', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # get token
        data = {'username': 'test_user', 'email': 'test@gmail.com', 'password': '12345'}
        response = self.client.post('http://127.0.0.1:8000/token', data)
        self.assertTrue('access' in response.data and 'refresh' in response.data)
        # get token with invalid username
        data = {'username': 't', 'email': 'test@gmail.com', 'password': '12345'}
        response = self.client.post('http://127.0.0.1:8000/token', data)
        self.assertFalse('access' in response.data and 'refresh' in response.data)
        # get token with invalid password
        data = {'username': 'test_user', 'email': 'test@gmail.com', 'password': '125'}
        response = self.client.post('http://127.0.0.1:8000/token', data)
        self.assertFalse('access' in response.data and 'refresh' in response.data)
