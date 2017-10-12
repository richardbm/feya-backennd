from rest_framework import views, status, permissions, viewsets
from rest_framework.response import Response
from sysadmin import serializers as sysadmin_serializers
from rest_framework.authtoken.models import Token
from accounts import models as accounts_models


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = accounts_models.Membership.objects.all()
    permission_classes = (permissions.IsAdminUser,)