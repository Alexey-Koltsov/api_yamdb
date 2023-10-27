from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                       ReviewViewSet, TitleViewSet, UserViewSet, get_token,
                       signup)


app_name = 'api'

router_api_01 = DefaultRouter()

router_api_01.register('users', UserViewSet, basename='users')
router_api_01.register('genres', GenreViewSet, basename='genres')
router_api_01.register('categories', CategoryViewSet, basename='categories')
router_api_01.register('titles', TitleViewSet, basename='titles')
router_api_01.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_api_01.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/auth/signup/', signup, name='signup'),
    path('v1/auth/token/', get_token, name='token'),
    path('v1/', include(router_api_01.urls)),
]
