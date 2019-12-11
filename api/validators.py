from rest_framework.permissions import BasePermission, SAFE_METHODS


class AppPermision(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated or request.method in SAFE_METHODS:
            return True
        return False


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.user.admin:
            return True
        return False
