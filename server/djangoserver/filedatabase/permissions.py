from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if IsAuthenticated:
            return obj.owner == request.user
        else:
            return False


