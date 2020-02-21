from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, post):
        if request.method in permissions.SAFE_METHODS:
            return True
        return post.author == request.user
