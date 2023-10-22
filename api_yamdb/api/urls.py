from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                       ReviewViewSet, TitleViewSet, TokenCreate, UserCreate, UserCreateList,)

# ProfileRetrieveUpdateDestroy, UserMeRetrieveUpdate,

router_api_01 = routers.DefaultRouter()
router_api_01.register(r'genres', GenreViewSet)
router_api_01.register(r'categories', CategoryViewSet)
router_api_01.register(r'titles', TitleViewSet)
router_api_01.register('auth/signup', UserCreate, basename='signup')
router_api_01.register('auth/token', TokenCreate, basename='token_obtain')
router_api_01.register('users', UserCreateList, basename='users')
# router_api_01.register('users/<slug:username>', ProfileRetrieveUpdateDestroy, basename='username')
# router_api_01.register('users/me', UserMeRetrieveUpdate, basename='userme')
router_api_01.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='comment')
router_api_01.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment')

urlpatterns = [
    path('v1/', include(router_api_01.urls)),
]
