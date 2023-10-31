from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MaxLengthValidator, RegexValidator
from django.utils import timezone
from rest_framework import serializers

from reviews.models import Category, Comment, Genre, Review, Title, User
from api_yamdb.settings import MAX_LEN_EMAIL, MAX_LEN_USERNAME


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User (пользователь).
    """

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'bio',
            'role'
        )


class UserRegistrationSerializer(serializers.Serializer):
    """
    Сериализатор для регистрации нового пользователя.
    """

    username = serializers.CharField(
        validators=[
            UnicodeUsernameValidator,
            MaxLengthValidator(MAX_LEN_USERNAME),
            RegexValidator(
                r'^[\w-]+$',
                'Недопустимый символ.'
            )
        ]
    )
    email = serializers.EmailField(
        validators=[MaxLengthValidator(MAX_LEN_EMAIL)]
    )

    def validate_username(self, value):
        if value.lower() == 'me':
            raise serializers.ValidationError(
                'Нельзя использовать имя пользователя "me".'
                'Выберите другое имя пользователя.'
            )
        return value

    def validate(self, data):
        if (User.objects.filter(username=data['username']).exists()
           ^ User.objects.filter(email=data['email']).exists()):
            raise serializers.ValidationError(
                'Пользователь с таким именем или email уже существует'
            )
        return data


class UserEditSerializer(serializers.ModelSerializer):
    """
    Сериализатор для редактирования информации пользователя.
    """

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )
        read_only_fields = ('role',)


class TokenSerializer(serializers.Serializer):
    """
    Сериализатор для создания токенов.
    """

    username = serializers.CharField()
    confirmation_code = serializers.CharField()


class GenreSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Genre (жанр).
    """

    class Meta:
        model = Genre
        fields = (
            'name',
            'slug'
        )


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Category (категория).
    """

    class Meta:
        model = Category
        fields = (
            'name',
            'slug'
        )


class TitleSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Title.
    """

    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'description',
            'category',
            'genre'
        )

    def validate_year(self, value):
        print(f'value: {value}')
        print(f'timezone.now().year: {timezone.now().year}')
        if value and value > timezone.now().year:
            raise serializers.ValidationError(
                {'year': 'Год не может быть больше текущего.'}
            )
        return value

    def to_representation(self, instance):
        return TitleReadSerializer(instance).data


class TitleReadSerializer(serializers.ModelSerializer):
    """
    Сериализатор для чтения информации о Title (произведение).
    """

    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(
        many=True,
        read_only=True
    )
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'description',
            'year',
            'category',
            'genre',
            'rating'
        )


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Comment (комментарий).
    """

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'text',
            'pub_date'
        )


class ReviewSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Review (отзыв).
    """

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Review
        fields = (
            'id',
            'text',
            'author',
            'score',
            'pub_date'
        )
