from rest_framework import serializers

class AddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    street = serializers.CharField(max_length=255)
    number = serializers.IntegerField(max_length=10)
    cep = serializers.IntegerField(max_length=10)