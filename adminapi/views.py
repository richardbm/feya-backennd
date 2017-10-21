from django.contrib.contenttypes import models
from django.core import exceptions
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from adminapi import registry
from adminapi import serializers
from ministry.models import DateContact


class ModelDoesNotExist(APIException):
    status_code = 400
    default_detail = "Model or App does not exist"


class GenericViewSet(viewsets.ModelViewSet):
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    search_fields = None

    def filter_queryset(self, queryset):
        self.search_fields = self.get_fields()
        self.filter_fields = self.get_fields_serializer()
        return super().filter_queryset(queryset)

    def get_fields(self):
        fields = self.get_queryset().model._meta.fields
        list_fields = []
        for obj in fields:
            if obj.is_relation is False:
                list_fields.append(obj.name)
        return list_fields

    def get_fields_serializer(self):
        serializer = self.get_serializer_class()
        dict_fields = serializer().get_fields()
        fields = tuple(dict_fields.keys())
        return fields

    def get_queryset(self):
        model_name = self.request.resolver_match.kwargs.get("model_name")
        app_name = self.request.resolver_match.kwargs.get("app_name")
        try:
            queryset = models.ContentType.objects.get(
                app_label=app_name,
                model=model_name
            ).model_class().objects.all()
            return queryset
        except exceptions.ObjectDoesNotExist:
            raise ModelDoesNotExist()

    def get_serializer_class(self):
        model_name = self.request.resolver_match.kwargs.get("model_name")
        app_name = self.request.resolver_match.kwargs.get("app_name")
        serializer = registry.serializer_registry.get(
            model_name,
            serializers.GenericSerializer
        )
        try:
            model = models.ContentType.objects.get(
                app_label=app_name,
                model=model_name
            ).model_class()
            serializer.Meta.model = model
            return serializer
        except exceptions.ObjectDoesNotExist:
            raise ModelDoesNotExist()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        depth = int(request.GET.get("depth", 0))
        fields = request.GET.get("fields", None)
        if fields:
            fields = fields.split(",")

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True,
                                             depth=depth, fields=fields)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True,
                                         depth=depth, fields=fields)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        depth = int(request.GET.get("depth", 0))
        fields = request.GET.get("fields", None)
        if fields:
            fields = fields.split(",")
        serializer = self.get_serializer(instance,
                                         depth=depth, fields=fields)
        return Response(serializer.data)


class DateContactView(viewsets.ModelViewSet):
    queryset = DateContact.objects.all()
    serializer_class = serializers.DateContactSerializer
    http_method_names = ('get',)
    filter_backends = []
    filter_fileds = []
    search_fields = []

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        instance = queryset.order_by("-date")[0]

        depth = int(request.GET.get("depth", 0))
        fields = request.GET.get("fields", None)
        if fields:
            fields = fields.split(",")

        serializer = self.get_serializer(instance,
                                         depth=depth, fields=fields)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        depth = int(request.GET.get("depth", 0))
        fields = request.GET.get("fields", None)
        if fields:
            fields = fields.split(",")
        serializer = self.get_serializer(instance,
                                         depth=depth, fields=fields)
        return Response(serializer.data)



