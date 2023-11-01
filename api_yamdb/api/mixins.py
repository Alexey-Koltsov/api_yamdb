<<<<<<< HEAD
from rest_framework import status, filters
=======
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
<<<<<<< HEAD
    UpdateModelMixin
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.permissions import IsAdminOrReadOnly

=======
)
from rest_framework.viewsets import GenericViewSet

>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed

class CreateDeleteViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin
):
    pass
<<<<<<< HEAD


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
    
=======
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
