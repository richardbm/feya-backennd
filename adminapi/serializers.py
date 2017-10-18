import types

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import models

from rest_framework import serializers, exceptions


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        if validated_data.get('username', None) is None:
            raise serializers.ValidationError(
                {'username': ['This field is required.']}
            )

        instance.username = validated_data['username']
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']

        if validated_data.get('password', None) is not None:
            instance.set_password(validated_data['password'])

        instance.save()

        return instance

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            )
        write_only_fields = ('password',)
        read_only_fields = (
            'is_staff',
            'is_superuser',
            'is_active',
            'date_joined',
            )


class GenericSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        depth = kwargs.pop('depth', None)
        super(GenericSerializer, self).__init__(*args, **kwargs)
        if depth is not None:
            self.Meta.depth = depth
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = None
        fields = '__all__'
