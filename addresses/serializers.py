from rest_framework import serializers
from addresses.models import Addresses

class AddressesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    street = serializers.CharField(max_length=255)
    number = serializers.IntegerField(max_length=10)
    cep = serializers.IntegerField(max_length=10)