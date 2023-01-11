from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from .models import User, Reservations_users_rooms
from rooms.serializers import RoomSerializer
import ipdb
from datetime import date
from rooms.utils import get_dates_interval


class UserSerializer(ModelSerializer):
    email = serializers.EmailField(
        max_length=100,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="Email already exists.",
            )
        ],
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_legal",
            "is_superuser",
            "created_at",
            "updated_at",
            # "reservations",
        ]
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = [
            "id",
            "is_active",
            "is_superuser",
            "created_at",
            "updated_at",
            # "reservations",
        ]

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance

class Reservations_users_rooms_Serializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Reservations_users_rooms    
        fields = ["id", "user", "room", "checkin_date", "checkout_date"]
        read_only_fields = ["created_at", "updated_at", "user"]