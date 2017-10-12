from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from accounts.models import User
from rest_framework import status


class AuthTestCase(APITestCase):

    def setUp(self):
        self.c = APIClient()

    def test_signup(self):
        data = {
            "first_name": "richard",
            "last_name": "barrios",
            "email": "rr@gg.cc",
            "phone": "04145550123",
            'address': "14av 15st doral",
            "password": "hobox1o1",
        }
        data_response = {
            "email": "rr@gg.cc",
        }
        response = self.c.post('/signup/', data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED, response.data)

        data_response_server = response.data.copy()

        data_response_server.pop('id')
        self.assertDictEqual(data_response, data_response_server, data_response_server)


    def test_failure_email_missing(self):
        data = {
            "password": "hobox1o1",
        }
        response = self.c.post('/login/', data, format='json')
        self.assertEqual(response.status_code, 400, "Debe devolver 400")

    def test_failure_password_missing(self):
        data = {
            "email": "johndoe",
        }
        response = self.c.post('/login/', data, format='json')
        self.assertEqual(response.status_code, 400, "Debe devolver 400")