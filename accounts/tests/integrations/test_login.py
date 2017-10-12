from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from accounts.models import User
from rest_framework import status
from django.contrib.auth.hashers import make_password

class AuthTestCase(APITestCase):

    def setUp(self):
        self.c = APIClient()
        User.objects.create(email='rr@gg.cc', password=make_password('hobox1o1'))

    def test_login(self):
        data = {
            "email": "rr@gg.cc",
            "password": "hobox1o1",
        }
        response = self.c.post('/login/', data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK, response.data)
        self.assertIn('token', response.data.keys(), 'falta el token de autenticacion')


    def test_failure_email_missing(self):
        data = {
            "password": "hobox1o1",
        }
        response = self.c.post('/login/', data, format='json')
        self.assertEqual(response.status_code, 400, "Debe devolver 400")

    def test_failure_password_missing(self):
        data = {
            "email": "john",
        }
        response = self.c.post('/login/', data, format='json')
        self.assertEqual(response.status_code, 400, "Debe devolver 400")