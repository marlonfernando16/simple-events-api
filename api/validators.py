from rest_framework.permissions import BasePermission, SAFE_METHODS


class AppPermision(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated or request.method in SAFE_METHODS:
            return True
        return False


class IsAuthentictedAndIsAdminOrReadyOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
            and request.user.admin
        )
