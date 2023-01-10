from .models import User, Reservations_users_rooms
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer, Reservations_users_rooms_Serializer
from .permissions import IsAccountOwner, IsAdminOrReadOnly
from rest_framework import generics, status
import ipdb
from rooms.models import Room
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError


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

        room_obj = get_object_or_404(Room, id=self.request.data["room"])

        checkin = self.request.data["checkin_date"]

        checkout = self.request.data["checkout_date"]

        reservation = Reservations_users_rooms.objects.filter(
            room=room_obj,
            checkin_date__range=[checkin, checkout],
            checkout_date__range=[checkin, checkout],
        ).exists()

        if reservation:
            raise ValidationError(
                {"detail": "room not available"}, status.HTTP_400_BAD_REQUEST
            )

        serializer.save(user=self.request.user, room=room_obj)

    def get_queryset(self):
        queryset = Reservations_users_rooms.objects.filter(user=self.request.user)

        return queryset


class ReservationsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservations_users_rooms.objects.all()
    permission_classes = []

    serializer_class = Reservations_users_rooms_Serializer
