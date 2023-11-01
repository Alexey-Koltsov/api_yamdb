from rest_framework import status, filters
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    UpdateModelMixin
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.permissions import IsAdminOrReadOnly


class CreateDeleteViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin
):
    pass


class CustomUpdateMixin(UpdateModelMixin):
    def update(self, request, *args, **kwargs):
        if request.method == 'PUT':
            return Response(
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        return super().update(request, *args, kwargs)


class GenreCategoryViewSetMixin:
    permission_classes = (IsAdminOrReadOnly,)
    search_fields = ('name',)
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
