from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from api.views import GenreViewSet, CategoryViewSet, TitleViewSet, ReviewViewSet, CommentViewSet, TokenCreate, UserCreate, UserCreateListViewSet, UserMeRetrieveUpdate, UserRetrieveUpdateDestroy

app_name = 'api'

router_api_01 = routers.DefaultRouter()
router_api_01.register('genres', GenreViewSet, basename='genres')
router_api_01.register('categories', CategoryViewSet,basename='categories')
router_api_01.register('titles', TitleViewSet, basename='titles')
router_api_01.register('auth/signup', UserCreate, basename='signup')
router_api_01.register('auth/token', TokenCreate, basename='token_obtain')
router_api_01.register('users', UserCreateListViewSet, basename='users')
#router_api_01.register('users/me', UserMeRetrieveUpdateViewSet,
#                       basename='usersme')
router_api_01.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews')
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