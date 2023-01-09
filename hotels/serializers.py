from rest_framework import serializers
from .models import Hotel
from addresses import seralizers
from addresses.models import Address
from feedbacks.serializers import FeedbackSerializer
from rest_framework.exceptions import ValidationError
import ipdb


class HotelSerializer(serializers.ModelSerializer):
    address = seralizers.AddressSerializer()
    feedbacks = FeedbackSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ["id", "name", "owner", "address", "feedbacks"]
        read_only_fields = ["owner", "feedbacks"]

    def create(self, validated_data):
        address_dict = validated_data.pop("address")

        already_exists = Address.objects.filter(
            cep=address_dict["cep"],
            number=address_dict["number"],
        ).exists()

        if already_exists:
            raise ValidationError({"detail": "Address already been taken."})

        address_obj = Address.objects.create(**address_dict)
        hotel_obj = Hotel.objects.create(**validated_data, address=address_obj)
        return hotel_obj
