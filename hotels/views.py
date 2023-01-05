from django.shortcuts import render
from rest_framework import generics
from .serializers import HotelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Hotel
import ipdb


class ListCreateHotelView(generics.ListCreateAPIView):

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RetrieveHotelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
