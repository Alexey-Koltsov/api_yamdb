from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins, viewsets


class ListCreateDestroyViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    pass

class CustomUpdateMixin(mixins.UpdateModelMixin):
    def update(self, request, *args, **kwargs):
        if request.method == 'PUT':
            return Response(
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        return super().update(request, *args, kwargs)