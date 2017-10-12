from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from rest_framework import serializers
from accounts import models as accounts_models
from django.contrib.auth.hashers import make_password


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        fields = ('id', 'email', 'password',)
        model = accounts_models.User
        extra_kwargs = {
            'id': {'read_only': True}
        }


    def create(self, validated_data):
        instance = super(SignUpSerializer, self).create(validated_data)
        instance.password = make_password(instance.password)
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'email', 'first_name', 'last_name', 'phone',)
        model = accounts_models.User
        extra_kwargs = {
            'id': {'read_only': True},
        }

