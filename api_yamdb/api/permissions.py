from rest_framework import permissions

<<<<<<< HEAD
from reviews.models import User


class IsAdmin(permissions.BasePermission):
    """
    Проверка: запрос произведен админом или суперпользователем.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role == User.ADMIN or request.user.is_superuser)
=======

def check_admin(request):
    """Проверка: запрос произведен админом."""

    return (request.user.is_authenticated
            and (request.user.is_admin or request.user.is_superuser))


class IsAdmin(permissions.BasePermission):
    """Проверка: запрос произведен админом или суперпользователем."""

    def has_permission(self, request, view):
        return check_admin(request)
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Проверка: безопасный запрос или запрос произведен админом
    или суперпользователем.
    """

    def has_permission(self, request, view):
<<<<<<< HEAD
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated and (
                request.user.role == User.ADMIN or request.user.is_superuser))
        )
=======
        return (request.method in permissions.SAFE_METHODS
                or check_admin(request))
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed


class IsAuthorModeratorAdminOrReadOnly(permissions.BasePermission):
    """
    Проверка: безопасный запрос или запрос
    произведен автором, модератором или админом.
    """

    def has_object_permission(self, request, view, obj):
<<<<<<< HEAD
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.role == User.ADMIN
            or request.user.role == User.MODERATOR
            or obj.author == request.user
        )

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )
    
=======
        return (request.method in permissions.SAFE_METHODS
                or check_admin(request)
                or request.user.is_moderator
                or obj.author == request.user)
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
