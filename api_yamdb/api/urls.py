from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import GenreViewSet, CategoryViewSet, TitleViewSet

router = DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'titles', TitleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
