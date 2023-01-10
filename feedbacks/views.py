from django.shortcuts import render
from rest_framework import generics
from .serializers import FeedbackSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Feedback
from hotels.models import Hotel
from django.shortcuts import get_object_or_404
import ipdb


class ListCreateFeedback(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        hotel_id = self.kwargs["pk"]
        hotel = get_object_or_404(Hotel, pk=hotel_id)
        serializer.save(owner=self.request.user, hotel_id=hotel.id)

    def get_queryset(self):
        hotel_id = self.kwargs["pk"]
        hotel = get_object_or_404(Hotel, pk=hotel_id)

        queryset = Feedback.objects.filter(hotel=hotel)

        return queryset


class RetrieveFeedback(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
