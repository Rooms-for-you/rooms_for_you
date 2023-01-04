from rest_framework import serializers
from .models import Hotel
from adresses.seralizers import AddressSerializer

class HotelSerializer(serializers.ModelSerializer):
    address = AddressSerializer

    class Meta:
        model = Hotel
        fields = ["id", 'owner', 'address']
        read_only_fields = ['owner']