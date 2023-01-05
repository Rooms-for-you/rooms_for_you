from django.shortcuts import render
from rest_framework import generics
from .serializers import HotelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Hotel
from .permissions import IsAccountOwner
from .permissions import IsLegalOrAdmin
import ipdb


class ListCreateHotelView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLegalOrAdmin]

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RetrieveHotelView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
