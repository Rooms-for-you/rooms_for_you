from rest_framework import serializers
from .models import Hotel
from addresses import seralizers
from addresses.models import Address
from feedbacks.serializers import FeedbackSerializer
import ipdb


class HotelSerializer(serializers.ModelSerializer):
    address = seralizers.AddressSerializer()
    feedbacks = FeedbackSerializer(many=True)

    class Meta:
        model = Hotel
        fields = ["id", "owner", "address", "feedbacks"]
        read_only_fields = ["owner", "feedbacks"]

    def create(self, validated_data):
        address_dict = validated_data.pop("address")
        address_obj = Address.objects.create(**address_dict)
        hotel_obj = Hotel.objects.create(**validated_data, address=address_obj)
        return hotel_obj
