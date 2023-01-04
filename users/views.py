from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwner, IsAdminOrReadOnly
from rest_framework import generics
import ipdb


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

    lookup_url_kwarg = "pk"

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance
        # ipdb.set_trace()
