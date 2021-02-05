from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_staff
        )


class IsAdminOrCreateOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method == 'POST' or
            request.user and request.user.is_staff
        )


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.access_right > 0
        )


class GetPatchPostForAuthUsers(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'PATCH', 'POST']:
            return bool(request.user and request.user.is_authenticated)
        return False


class IsAuthForGetOrCreateOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method == 'POST' or
            request.method == 'GET' and request.user and request.user.is_authenticated
        )
