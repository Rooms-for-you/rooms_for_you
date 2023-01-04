from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:

        if request.method in permissions.SAFE_METHODS:
            if request.user.is_authenticated:
                if request.user.is_superuser:
                    return True

        if request.method == "POST":
            return True


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        if request.user.is_authenticated:
            return obj == request.user or request.user.is_superuser
