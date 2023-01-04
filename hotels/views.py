from django.shortcuts import render
from rest_framework import generics
from .serializers import HotelSerializer
from .models import Hotel


class ListCreateHotelView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = MovieSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RetrieveHotelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
