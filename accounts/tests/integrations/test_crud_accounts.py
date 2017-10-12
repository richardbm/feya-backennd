from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from accounts.models import User
from rest_framework import status
from django.contrib.auth.hashers import make_password


class AuthTestCase(APITestCase):

    def setUp(self):
        self.c = APIClient()
        self.email = "rr@gg.cc"
        self.password = 'hobox1o1'
        self.phone = "12345678"
        self.address = "14av 15st doral"
        data = {
            'first_name': "Richard",
            'last_name': "Barrios",
            'phone': self.phone,
            'email': self.email,
            'password': make_password(self.password),
            'address': self.address
        }
        user = User(**data)
        user.save()

    def test_get_account(self):
        self.c.login(email=self.email, password=self.password)
        response = self.c.get('/profile/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = {
            'first_name': "Richard",
            'last_name': "Barrios",
            'phone': self.phone,
            'email': self.email,
            'address': self.address

        }
        data_response = response.data.copy()

        data_response.pop('id')
        self.assertDictEqual(data, data_response)

    def test_get_account_not_auth(self):
        response = self.c.get('/profile/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, "no debe mostrar ninguna cuenta")

    def test_put_account(self):
        data = {
            'first_name': "Richard2",
            'last_name': "Barrios2",
            'phone': self.phone+"2",
            'email': self.email+"c",
            'address': self.address+"c"

        }
        self.c.login(email=self.email, password=self.password)
        response = self.c.put('/profile/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        data_response = response.data.copy()

        data_response.pop('id')

        self.assertDictEqual(data, data_response)

    def test_put_account_not_auth(self):
        data = {
            'first_name': "Richard2",
            'last_name': "Barrios2",
            'phone': self.phone+"2",
            'email': self.email+"c",
            'address': self.address + "c"

        }
        response = self.c.put('/profile/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, "no debe mostrar ninguna cuenta")