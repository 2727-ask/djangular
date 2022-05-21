from rest_framework.permissions import BasePermission, SAFE_METHODS


class CategoryPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_authenticated and request.user.is_superuser:
            return True
        else:
            return False
