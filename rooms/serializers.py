from rest_framework import serializers
from rooms.models import Room
from services.models import Service
from services.serializers import ServiceSerializer
from hotels.serializers import HotelSerializer
from datetime import date, timedelta
from .utils import get_dates
import ipdb

class RoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    number = serializers.IntegerField()
    beds = serializers.IntegerField()
    ranking = serializers.CharField(max_length=255)
    hotel = HotelSerializer(read_only=True)
    services = ServiceSerializer(many=True)
    unavailable_days = serializers.SerializerMethodField()

    def get_unavailable_days(self, obj:dict):

        unavailable_days = {}

        lista_datas = get_dates(obj.reservations_users_rooms_set.all())

        for data in lista_datas:

            if not str(data.year) in unavailable_days: 
                unavailable_days.update({str(data.year):{}})
                
            if not str(data.month) in unavailable_days[str(data.year)]:
                unavailable_days[str(data.year)].update({str(data.month): []})

            if str(data.year) in unavailable_days and str(data.month) in unavailable_days[str(data.year)]:
                if not data.day in unavailable_days[str(data.year)][str(data.month)]:
                    unavailable_days[str(data.year)][str(data.month)].append(data.day)
                    unavailable_days[str(data.year)][str(data.month)] = sorted(unavailable_days[str(data.year)][str(data.month)])

            keys = list(unavailable_days[str(data.year)].keys())    
            sorted_keys = sorted(keys)
            sorted_dict = {i: unavailable_days[str(data.year)][i] for i in sorted_keys}
            unavailable_days[str(data.year)] = sorted_dict
            

        return unavailable_days


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