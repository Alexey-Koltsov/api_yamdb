from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from rest_framework.routers import DefaultRouter
from api.views import UserCreate, UserCreateList, GenreViewSet, CategoryViewSet, TitleViewSet, ReviewViewSet, CommentViewSet


router_api_01 = routers.DefaultRouter()
router_api_01.register(r'genres', GenreViewSet)
router_api_01.register(r'categories', CategoryViewSet)
router_api_01.register(r'titles', TitleViewSet)
router_api_01.register('auth/signup', UserCreate, basename='signup')
router_api_01.register('users', UserCreateList, basename='users')
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
    path('v1/auth/token/', TokenObtainPairView.as_view(),
         name='token_obtain'),
  path('', include(router.urls)),
]
