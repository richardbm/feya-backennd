from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from accounts.models import User
from rest_framework import status
from django.contrib.auth.hashers import make_password

class AuthTestCase(APITestCase):
    def setUp(self):
        self.c = APIClient()
        self.email = 'rhrichardbm@gmail.com'
        self.user = created = User.objects\
                .create(email=self.email, password=make_password('hobox1o1'))


    def test_request_recover_password(self):
        data = {'email':self.email}
        response = self.c.post('/request-recover-password/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.status_code)

        self.assertIn("detail", response.data.keys(), response.data.keys())
        detail = response.data.get('detail')
        msg_detail = u"se ha enviado un email con el código de recuperación"
        self.assertIn(msg_detail, detail, detail)

        user = User.objects.get(email=self.email)
        self.assertTrue(hasattr(user, 'recovery_code'))
        self.assertEqual(len(user.recovery_code), 6, 'debe generar un código aleatorio de 6 dígitos')

    def test_recover_password(self):
        code = "ABC123"
        user = self.user
        user.recovery_code = code
        user.save()

        data = {
            'recovery_code': code,
            'password': "hobox1o1"
        }
        response = self.c.post('/recover-password/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        self.assertIn("detail", response.data.keys(), response.data.keys())
        detail = response.data.get('detail')
        msg_detail = u"la contraseña ha sido cambiada"
        self.assertIn(msg_detail, detail, detail)

        user = User.objects.get(email=self.email)
        self.assertEqual(user.recovery_code, None, 'debe eliminar el código luego de cambiar la contraseña')

    def test_recover_password_fail(self):
        code = "ABC123"
        user = self.user
        user.recovery_code = code
        user.save()

        data = {
            'recovery_code': code
        }
        response = self.c.post('/recover-password/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, 'debe fallar por no enviar la contraseña')

        self.assertIn("detail", response.data.keys(), response.data.keys())
        detail = response.data.get('detail')
        msg_detail = u"Debe enviar la contraseña"
        self.assertIn(msg_detail, detail, detail)

        data = {
            'password': "hobox1o1"
        }
        response = self.c.post('/recover-password/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, 'debe fallar por no enviar el código')

        self.assertIn("detail", response.data.keys(), response.data.keys())
        detail = response.data.get('detail')
        msg_detail = u"Debe enviar el código"
        self.assertIn(msg_detail, detail, detail)




