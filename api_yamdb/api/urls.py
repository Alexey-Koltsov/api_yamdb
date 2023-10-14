from django.urls import path, include

from .views import ReviewViewSet, CommentViewSet

router = SimpleRouter()
router.register('reviews', ReviewViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]