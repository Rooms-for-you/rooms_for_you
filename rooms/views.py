from .models import Room
from .serializers import RoomSerializer
from .permissions import IsAccountOwner
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics


class RoomView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    # def perform_create(self, serializer):
    #    serializer.save(owner_id=self.request.owner.id)

class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]

    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    