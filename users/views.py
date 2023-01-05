from .models import User, Reservations_users_rooms
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer, Reservations_users_rooms_Serializer
from .permissions import IsAccountOwner, IsAdminOrReadOnly
from rest_framework import generics
import ipdb
from rooms.models import Room
from django.core.exceptions import ObjectDoesNotExist


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

    def get_queryset(self):
        queryset = Reservations_users_rooms.objects.filter(user=self.request.user)

        return queryset


class ReservationsDetailView(generics.RetrieveDestroyAPIView):
    queryset = Reservations_users_rooms.objects.all()
    permission_classes = []

    serializer_class = Reservations_users_rooms_Serializer
