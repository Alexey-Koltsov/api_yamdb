from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from review.models import Comment, Review, User

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        read_only_fields = ('post', 'author')


class ReviewSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(read_only=True,
                            default=serializers.CurrentUserDefault(),
                            slug_field='username')
    review = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all())
