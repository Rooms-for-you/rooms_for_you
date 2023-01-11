from .models import User, Reservations_users_rooms
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer, Reservations_users_rooms_Serializer
from .permissions import IsAccountOwner, IsAdminOrReadOnly
from rest_framework import generics, status
import ipdb
from rooms.models import Room
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from datetime import date, datetime, timedelta
from rooms.utils import get_dates_interval


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance


class ReservationsView(generics.ListCreateAPIView):
    queryset = Reservations_users_rooms.objects.all()
    permission_classes = []

    serializer_class = Reservations_users_rooms_Serializer

    def perform_create(self, serializer):
        room_id = self.request.data.get('room')
        room_obj = get_object_or_404(Room, id=room_id)

        queryset = Reservations_users_rooms.objects.filter(room=room_obj)

        checkin = datetime.strptime(self.request.data.get("checkin_date"), '%Y-%m-%d')

        checkout = datetime.strptime(self.request.data.get("checkout_date"), '%Y-%m-%d')

        if checkin > checkout:
            raise ValidationError(
                {"detail": "checkout_date must be greater than checkin_date, or create a time machine"}, status.HTTP_401_UNAUTHORIZED
            )

        if checkin.date() < datetime.now().date():
            raise ValidationError(
                {"detail": "checkin_date must NOT be greater than the current date, do you want to go back in time?"}, status.HTTP_401_UNAUTHORIZED
            )

        if checkout == checkin :
            raise ValidationError(
                {"detail": "Your reservation must last for a minimum of one day"}, status.HTTP_401_UNAUTHORIZED
            )

        occupied_dates = []

        if len(queryset) > 0:
            for reservation in queryset:
                days_list = get_dates_interval(reservation.checkin_date, reservation.checkout_date - timedelta(days=1))
                for day in days_list:
                    occupied_dates.append(day)


        if checkin.date() in occupied_dates or checkout.date() in occupied_dates:
            raise ValidationError(
                {"detail": "room not available"}, status.HTTP_401_UNAUTHORIZED
            )
            
        serializer.save(user=self.request.user, room=room_obj)

            
    def get_queryset(self):
        queryset = Reservations_users_rooms.objects.filter(user=self.request.user)

        return queryset 


class ReservationsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservations_users_rooms.objects.all()
    permission_classes = []

    serializer_class = Reservations_users_rooms_Serializer
