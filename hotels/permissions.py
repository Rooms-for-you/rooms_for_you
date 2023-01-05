from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User


class IsLegalOrAdmin(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:

        if request.method in permissions.SAFE_METHODS:
            if request.user.is_authenticated:
                if request.user.is_superuser:
                    return True
                elif request.user.is_legal:
                    return True
    


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        if request.user.is_authenticated:
            return obj == request.user or request.user.is_superuser
