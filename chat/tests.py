from rest_framework import status
from rest_framework.test import APITestCase

DATA = {
    'email': 'test@gmail.com',
    'author': 'My_username',
    'message': 'hello world'
}


class MessagesTestCase(APITestCase):
    """Messages test case"""

    def test_create_message(self):
        """Test  of creating messages"""
        # create message test
        response = self.client.post('https://publicchatroomtask.herokuapp.com/api/messages/', data=DATA)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_email(self):
        """Test send message with invalid email"""
        # empty email field test
        response = self.client.post('https://publicchatroomtask.herokuapp.com/api/messages/', data=DATA)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # invalid email
        DATA['email'] = 'invlaid.gmail.com'
        response = self.client.post('http://127.0.0.1:8000/api/messages/', data=DATA)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # empty email field test
        DATA['email'] = ''
        response = self.client.post('http://127.0.0.1:8000/api/messages/', data=DATA)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # invalid email test
        DATA['email'] = 'asd.@ewq.qwe'
        response = self.client.post('http://127.0.0.1:8000/api/messages/', data=DATA)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_message_body(self):
        """Test send message with invalid body"""
        DATA['email'] = 'test@gmail.com'
        # more than 100 chars in message test
        DATA['message'] *= 20
        response = self.client.post('http://127.0.0.1:8000/api/messages/', data=DATA)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # empty message test
        DATA['message'] = ''
        response = self.client.post('http://127.0.0.1:8000/api/messages/', data=DATA)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_message_by_id(self):
        """Test for getting single message"""
        # create message
        response = self.client.post('http://127.0.0.1:8000/api/messages/', data=DATA)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        message_id = response.data['id']

        # try to get message by id
        response = self.client.get(f'http://127.0.0.1:8000/api/messages/{message_id}/', data=DATA)
        self.assertEqual(response.data['email'], DATA['email'])
        self.assertEqual(response.data['message'], DATA['message'])
        self.assertEqual(response.data['id'], message_id)

    def test_not_allowed_methdos(self):
        """Test not allowed methods as put, delete; post for single message"""
        DATA['message'] = 'normal message'
        # create message
        response = self.client.post('http://127.0.0.1:8000/api/messages/', data=DATA)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        message_id = response.data['id']

        # try post method to single message
        response = self.client.post(f'http://127.0.0.1:8000/api/messages/{message_id}/', data=DATA)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        # try put method to single message
        response = self.client.put(f'http://127.0.0.1:8000/api/messages/{message_id}/', data=DATA)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        # try delete method to single message
        response = self.client.delete(f'http://127.0.0.1:8000/api/messages/{message_id}/', data=DATA)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_pagination(self):
        """Test pagination"""
        for i in range(25):
            DATA['message'] = 'a' * i
            response = self.client.post(f'http://127.0.0.1:8000/api/messages/', data=DATA)
        response = self.client.get("http://127.0.0.1:8000/api/messages/?page=2", data=DATA)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get("http://127.0.0.1:8000/api/messages/?page=3", data=DATA)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get("http://127.0.0.1:8000/api/messages/?page=12", data=DATA)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
