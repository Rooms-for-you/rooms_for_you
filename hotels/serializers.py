from rest_framework import serializers
from .models import Hotel
from addresses import seralizers
from addresses.models import Address
from feedbacks.serializers import FeedbackSerializer
from rest_framework.exceptions import ValidationError


class HotelSerializer(serializers.ModelSerializer):
    address = seralizers.AddressSerializer()
    feedbacks = FeedbackSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ["id", "name", "owner", "address", "feedbacks", "rooms"]
        read_only_fields = ["owner", "feedbacks","rooms"]
        depth = 2

    def create(self, validated_data):
        address_dict = validated_data.pop("address", None)

        already_exists = Address.objects.filter(
            cep=address_dict["cep"],
            number=address_dict["number"],
        ).exists()

        if already_exists:
            raise ValidationError({"detail": "Address already been taken."})

        address_obj = Address.objects.create(**address_dict)
        hotel_obj = Hotel.objects.create(**validated_data, address=address_obj)
        return hotel_obj

    def update(self, instance: Hotel, validated_data: dict):

        address_dict: dict = validated_data.pop("address", None)
        if address_dict:
            address_obj = Address.objects.filter(hotel=instance).first()

            for key, value in address_dict.items():
                setattr(address_obj, key, value)

            already_exists = Address.objects.filter(
            cep=address_obj.cep,
            number=address_obj.number,
            ).exists()

            if already_exists:
                raise ValidationError({"detail": "Address already been taken."})

            address_obj.save()

            

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance 
