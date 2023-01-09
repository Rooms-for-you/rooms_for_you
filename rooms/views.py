from .models import Room
from .serializers import RoomSerializer
from .permissions import IsAccountOwner
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from hotels.models import Hotel
from django.shortcuts import get_object_or_404
import ipdb

class RoomView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    def perform_create(self, serializer):
        hotel_id = self.kwargs['pk']
        hotel = get_object_or_404(Hotel, pk=hotel_id)
        serializer.save(hotel=hotel)

class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    