from rest_framework import status
from rest_framework.test import APITestCase


class PostTestCase(APITestCase):

    def test_post_unauthorized(self):
        """Test unauthorised"""
        response = self.client.post('http://127.0.0.1:8000/api/posts/', {}, HTTP_AUTHORIZATION='')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_one(self):
        """
        Post testing
        """
        # register user
        data = {'username': 'test_user', 'email': 'test@gmail.com', 'password': '12345'}
        response = self.client.post('http://127.0.0.1:8000/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # login user
        response = self.client.post('http://127.0.0.1:8000/api/login/', data)
        token = response.data['access']
        # create new post
        data = {'title': 'hello', 'body': 'world', 'token': token}
        response = self.client.post('http://127.0.0.1:8000/api/posts/',  data,
                                    HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.data['author'], 'test_user')
        # like post
        response = self.client.get('http://127.0.0.1:8000/api/posts/hello/like/', {},
                                   HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.data['response'], 'you like this post')
        # like count
        response = self.client.get('http://127.0.0.1:8000/api/posts/hello/', {},
                                   HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.data['like_count'], 1)
        # edit post
        data = {'title': 'hello-edited', 'body': 'new body'}
        response = self.client.put('http://127.0.0.1:8000/api/posts/hello/', data,
                                   HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.data['title'], 'hello-edited')
        self.assertEqual(response.data['body'], 'new body')

        # register new user
        data = {'username': 'test_user_new', 'email': 'test@gmail.com', 'password': '12345'}
        response = self.client.post('http://127.0.0.1:8000/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # login new user
        response = self.client.post('http://127.0.0.1:8000/api/login/', data)
        token = response.data['access']
        # like post
        response = self.client.get('http://127.0.0.1:8000/api/posts/hello-edited/like/', {},
                                   HTTP_AUTHORIZATION=f'Bearer {token}')
        # like count
        response = self.client.get('http://127.0.0.1:8000/api/posts/hello-edited/', {},
                                   HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.data['like_count'], 2)
        # unlike post
        response = self.client.get('http://127.0.0.1:8000/api/posts/hello-edited/unlike/', {},
                                   HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get('http://127.0.0.1:8000/api/posts/hello-edited/', {},
                                   HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.data['like_count'], 1)
        # try to delete post of another author
        response = self.client.delete('http://127.0.0.1:8000/api/posts/hello-edited/', {},
                                      HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # try to edit post of another author
        data = {'title': 'new_title'}
        response = self.client.put('http://127.0.0.1:8000/api/posts/hello-edited/', data,
                                   HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

