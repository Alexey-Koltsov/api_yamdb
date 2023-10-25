from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import permissions

User = get_user_model()


def get_user(request):
    return get_object_or_404(
        User,
        username=request.user.username
    )


class IsAdmin(permissions.BasePermission):
    """Проверка: запрос произведен администратором."""

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return False
        user = get_user(request)
        return (
            user.role == 'admin'
            or user.is_superuser
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    """Проверка: безопасный запрос или запрос произведен администратором."""

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return request.method in permissions.SAFE_METHODS
        user = get_user(request)
        return (
            request.method in permissions.SAFE_METHODS
            or user.role == 'admin'
            or user.is_superuser
        )


class IsAuthorModeratorAdminOrReadOnly(permissions.BasePermission):
    """
    Проверка: безопасный запрос или запрос произведен автором,
    модератором, администратором.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return request.method in permissions.SAFE_METHODS
        user = get_object_or_404(User, username=request.user.username)
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or user.role == 'moderator'
            or user.role == 'admin'
            or user.is_superuser
        )
    
class AuthorIsAuthenticatedModeratorAdminSuperuserOrReadOnly(permissions.BasePermission):
    def haspermission(self, request, view):
        return (
            request.method in permissions.SAFEMETHODS
            or request.user.isauthenticated)

    def hasobject_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFEMETHODS
            or obj.author == request.user or request.user.ismoderator
            or request.user.isadmin or request.user.issuperuser)