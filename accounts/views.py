from rest_framework import views, status, permissions
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
from rest_framework import views, status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from accounts import models as accounts_models
from accounts import serializers as accounts_serializers
from accounts.utils import send_email


class LoginView(views.APIView):
    serializer_class = accounts_serializers.AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class SignupView(views.APIView):
    serializer_class = accounts_serializers.SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProfileView(views.APIView):
    serializer_class = accounts_serializers.ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestRecoverPassword(views.APIView):
    def post(self, request, format=None):
        email = request.data.get('email', None)
        if not email:
            data = {
                'detail': u"Debe enviar el correo electrónico"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        user = accounts_models.User.objects.filter(email=email)
        if user.exists():
            user = user.first()
            code = self.set_code_recovery(user)
        else:
            data = {
                'detail': u"El correo electrónico no existe"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        self.send_email_recover_password(code, user)

        data = {
            'detail': u"se ha enviado un email con el código de recuperación"
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def set_code_recovery(self, user):
        while True:
            code = get_random_string(length=6, allowed_chars="1234ABCD")
            if not accounts_models.User.objects.filter(recovery_code=code).exists():
                user.recovery_code = code
                user.save()
                break
        return code

    def send_email_recover_password(self, code, user):
        subject, to = u"Iglesia Feya: Recuperación de Contraseña", user.email
        msg = "Introduzca este codigo en su aplicación para " \
              "continuar con el cambio de contraseña"
        template = 'email/template_email.html'
        data = {
            'subject': code,
            'message': msg
        }
        send_email(template, to, subject, data)


class RecoverPassword(views.APIView):
    def post(self, request, format=None):
        code = request.data.get('recovery_code', None)
        password = request.data.get('password', None)
        if not code:
            msg_detail = u"Debe enviar el código"

            data = {
                "detail": msg_detail
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        if not password:
            msg_detail = u"Debe enviar la contraseña"

            data = {
                "detail": msg_detail
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = accounts_models.User.objects.get(recovery_code=str(code).upper())
        except accounts_models.User.DoesNotExist:
            msg_detail = u"Código inválido"
            data = {
                "detail": msg_detail
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        user.password = make_password(password)
        user.recovery_code = None
        user.save()

        msg_detail = u"la contraseña ha sido cambiada"

        data = {
            "detail": msg_detail
        }
        return Response(data, status=status.HTTP_200_OK)
