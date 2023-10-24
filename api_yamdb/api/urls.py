from django.urls import include, path
from rest_framework import routers

from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                       ReviewViewSet, TitleViewSet, TokenCreate, UserCreate,
                       UserCreateListViewSet, UserMeRetrieveUpdate,
                       UserRetrieveUpdateDestroy,)


router_api_01 = routers.DefaultRouter()
router_api_01.register('auth/signup', UserCreate, basename='signup')
router_api_01.register('auth/token', TokenCreate, basename='token_obtain')
router_api_01.register('users', UserCreateListViewSet, basename='users')
#router_api_01.register('users/me', UserMeRetrieveUpdateViewSet,
#                       basename='usersme')
router_api_01.register(r'genres', GenreViewSet)
router_api_01.register(r'categories', CategoryViewSet)
router_api_01.register(r'titles', TitleViewSet)
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
    #path('v1/users/', UserCreateList.as_view()),
    path('v1/users/me/', UserMeRetrieveUpdate.as_view()),
    path('v1/users/<slug:username>/', UserRetrieveUpdateDestroy.as_view()),
]
