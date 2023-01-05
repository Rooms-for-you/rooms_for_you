from rest_framework import serializers
from rooms.models import Room
from services.models import Service
from services.serializers import ServiceSerializer

class RoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    number = serializers.IntegerField(max_length=10)
    beds = serializers.IntegerField(max_length=1)
    ranking = serializers.CharField(max_length=255)
    
    services = ServiceSerializer(many=True)

    def create(self, validated_data: dict) -> Room:
        services_list = validated_data.pop("services")
        room = Room.objects.create(**validated_data)

        for services_dict in services_list:
            services_obj = Service.objects.get_or_create(**services_dict)[0]
            room.services.add(services_obj)
        
        room.save()

        return room

    def update(self, instance: Room, validated_data: dict):

        services_list: dict = validated_data.pop("services", None)

        if services_list:
            new_service = []

            for service in services_list:
                services_obj, created = Service.objects.get_or_create(**service)
                new_service.append(services_obj)

            instance.services.set(new_service)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance      