from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Request permission from the client so that only the admins of the object can edit it and others can only read it.
    Assumes that the model instance has an `user` attribute
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool(request.user and request.user.is_staff)
    

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user