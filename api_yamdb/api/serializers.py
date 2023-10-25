import re

from django.db.models import Avg
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers, validators
from rest_framework.relations import SlugRelatedField
from reviews.models import Genre, Category, Title, Comment, Review

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для самостоятельной регистрации пользователей."""

    username = serializers.SlugField(
        max_length=150,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        max_length=254,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    confirmation_code = serializers.HiddenField(
        default='',
        write_only=True,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'confirmation_code')

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" запрещено!'
            )
        if not re.match(r'^[\w.@+-]+\Z', value):
            raise serializers.ValidationError(
                'Имя пользователя должно соотвестсвовать паттерну!'
            )
        return value


class TokenSerializer(serializers.ModelSerializer):
    """Сериализатор для создания токенов."""

    username = serializers.SlugField(
        max_length=150,
        required=True)
    confirmation_code = serializers.SlugField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')

    def validate_username(self, value):
        if not re.match(r'^[\w.@+-]+\Z', value):
            raise serializers.ValidationError(
                'Имя пользователя должно соответствовать паттерну!'
            )
        return value


class UserCreateListByAdminSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создание пользователя и
    получение списка пользователей Админом.
    """

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" запрещено!'
            )
        if not re.match(r'^[\w.@+-]+\Z', value):
            raise serializers.ValidationError(
                'Имя пользователя должно соответствовать паттерну!'
            )
        return value


class UserGetUpdateDeleteByAdminSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения, изменения и удаления
    пользователей по имени пользователя Админом.
    """

    username = serializers.SlugField(
        max_length=150,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        max_length=254,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    first_name = serializers.SlugField(
        max_length=150,
    )
    last_name = serializers.SlugField(
        max_length=150,
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" запрещено!'
            )
        if not re.match(r'^[\w.@+-]+\Z', value):
            raise serializers.ValidationError(
                'Имя пользователя должно соответствовать паттерну!'
            )
        return value


class UserMeGetUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения, изменения
    своих данных пользователями.
    """

    username = serializers.SlugField(
        max_length=150,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        max_length=254,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    first_name = serializers.SlugField(
        max_length=150,
    )
    last_name = serializers.SlugField(
        max_length=150,
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" запрещено!'
            )
        if not re.match(r'^[\w.@+-]+\Z', value):
            raise serializers.ValidationError(
                'Имя пользователя должно соответствовать паттерну!'
            )
        return value


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )
    rating = serializers.SerializerMethodField()
    
    class Meta:
        model = Title
        fields = '__all__'
    
    def get_rating(self, obj):
        if obj.reviews.count() == 0:
            return None
        rev = Review.objects.filter(title=obj).aggregate(rating=Avg('score'))
        return rev['rating']


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Comment


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    
    def validate_score(self, value):
        if 0 > value > 10:
            raise serializers.ValidationError('Оценка не может быть больше 10')
        return value
    
    def validate(self, data):
        request = self.context['request']
        author = request.user
        title_id = self.context.get('view').kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if (
            request.method == 'POST'
            and Review.objects.filter(title=title, author=author).exists()
        ):
            raise ValidationError('Отзыв уже есть!')
        return data
    
    class Meta:
        fields = '__all__'
        model = Review
      