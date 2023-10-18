from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from api.views import UserCreate


router_api_01 = routers.DefaultRouter()
router_api_01.register('auth/signup', UserCreate, basename='signup')

urlpatterns = [
    path('v1/', include(router_api_01.urls)),
    path('v1/auth/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
]
