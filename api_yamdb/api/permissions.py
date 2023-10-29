from rest_framework import permissions


def check_admin(request):
    """Проверка: запрос произведен админом."""

    return (request.user.is_authenticated
            and (request.user.is_admin or request.user.is_superuser))


class IsAdmin(permissions.BasePermission):
    """Проверка: запрос произведен админом или суперпользователем."""

    def has_permission(self, request, view):
        return check_admin(request)


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Проверка: безопасный запрос или запрос произведен админом
    или суперпользователем.
    """

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or check_admin(request))


class IsAuthorModeratorAdminOrReadOnly(permissions.BasePermission):
    """
    Проверка: безопасный запрос или запрос
    произведен автором, модератором или админом.
    """

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or check_admin(request)
                or request.user.is_moderator
                or obj.author == request.user)
