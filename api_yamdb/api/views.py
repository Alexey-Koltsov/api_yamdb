from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404

from api_yamdb.models import Review, Comment
from .serializers import (ReviewSerializer,
                          CommentSerializer)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
