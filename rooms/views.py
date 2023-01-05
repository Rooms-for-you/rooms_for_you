from .models import Room
from .serializers import RoomSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics

class RoomView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    # def perform_create(self, serializer):
    #    serializer.save(owner_id=self.request.owner.id)