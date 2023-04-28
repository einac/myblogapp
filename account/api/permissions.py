from rest_framework.permissions import BasePermission


class NotAuthenticated(BasePermission):
    message = "Zaten aktif bir kullanıcı hesabınız mevcut!"

    def has_permission(self, request, view):
        return not request.user.is_authenticated
