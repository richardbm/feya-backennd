from adminapi.serializers import UserSerializer
from django.contrib.contenttypes import models
from django.core import exceptions
from rest_framework import authentication
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from adminapi import registry
from adminapi import serializers


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.data
        del user['password']
        return Response(user)

    def list(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        for user in serializer.data:
            del user['password']
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        serializer = UserSerializer(self.get_object())
        user = serializer.data
        del user['password']
        return Response(user)

    def update(self, request, pk=None):
        serializer = UserSerializer(
            self.get_object(),
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.data
        del user['password']
        return Response(user)


class LoginView(APIView):
    authentication_classes = (authentication.BasicAuthentication,)

    def post(self, request, format=None):
        user = request.user
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "detail": "Credentials validated",
            "token": token.key,
            "username": request.user.username
         })


class ModelDoesNotExist(APIException):
    status_code = 400
    default_detail = "Model or App does not exist"


class GenericViewSet(viewsets.ModelViewSet):
    authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self):
        model_name = self.request.resolver_match.kwargs.get("model_name")
        app_name = self.request.resolver_match.kwargs.get("app_name")
        try:
            queryset = models.ContentType.objects.get(
                app_label=app_name,
                model=model_name
            ).model_class().objects.all()
            return queryset
        except (exceptions.ObjectDoesNotExist):
            raise ModelDoesNotExist()

    def get_serializer_class(self):
        model_name = self.request.resolver_match.kwargs.get("model_name")
        app_name = self.request.resolver_match.kwargs.get("app_name")
        serializer = registry.serializer_registry.get(
            model_name,
            serializers.GenericSerializer
        )
        model = None

        try:
            model = models.ContentType.objects.get(
                app_label=app_name,
                model=model_name
            ).model_class()
            serializer.Meta.model = model
            return serializer
        except (exceptions.ObjectDoesNotExist):
            raise ModelDoesNotExist()
