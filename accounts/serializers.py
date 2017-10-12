from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from rest_framework import serializers
from accounts import models as accounts_models
from django.contrib.auth.hashers import make_password

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"))
    password = serializers.CharField(label=_("Password"),
                                     style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password)

            if user:
                # From Django 1.10 onwards the `authenticate` call simply
                # returns `None` for is_active=False users.
                # (Assuming the default `ModelBackend` authentication backend.)
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg,
                                                      code='authorization')
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


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

