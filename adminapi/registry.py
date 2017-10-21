from adminapi import serializers

serializer_registry = {
    "default": serializers.GenericSerializer,
    "service": serializers.ServiceSerializer,
}
