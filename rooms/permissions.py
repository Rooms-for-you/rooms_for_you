from rest_framework import permissions
from users.models import User
from rest_framework.views import View, Request

class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        if request.user.is_authenticated:
            return obj.owner == request.user or request.user.is_superuser