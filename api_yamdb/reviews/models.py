from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models
from django.db.models import Avg
from django.utils import timezone
<<<<<<< HEAD

from api.constants import SYMBOLS_QUANTITY
from api_yamdb.settings import (
    MAX_LEN_EMAIL, MAX_LEN_NAME,
    MAX_LEN_ROLE, MAX_LEN_USERNAME
)
from reviews.basemodels import ModelPubDate, NameSlugBaseModel
from reviews.validators import creation_year_validator


class User(AbstractUser):
    """Модель User (пользователь)"""

    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'

    ROLE_CHOICES = [
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (USER, 'Пользователь'),
    ]
    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        unique=True,
        verbose_name='Имя пользователя',
        validators=[RegexValidator(
            r'^[\w-]+$', 'Недопустимый символ.'
        )],
    )
    email = models.EmailField(
        max_length=MAX_LEN_EMAIL,
        unique=True,
        verbose_name='Адрес электронной почты'
    )
    bio = models.TextField(
        blank=True,
        null=True,
        verbose_name='О себе'
    )
    role = models.CharField(
        max_length=MAX_LEN_ROLE,
        choices=ROLE_CHOICES,
        default=USER,
        verbose_name='Роль',
    )

    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)
        constraints = [
            models.CheckConstraint(
                name='cant_use_me_username',
                check=~models.Q(username='me'),
            ),
        ]

    def __str__(self):
        return self.username[:SYMBOLS_QUANTITY]

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR


class Genre(NameSlugBaseModel):
    """Модель Genre (жанр)"""

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Category(NameSlugBaseModel):
    """Модель Category (категория)"""

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Title(models.Model):
    """Модель Title(произведение)"""

    name = models.CharField(
        max_length=MAX_LEN_USERNAME,
        blank=False,
        verbose_name='Название произведения'
    )
    year = models.PositiveSmallIntegerField(
        validators=[creation_year_validator],
        blank=True,
        null=True,
        verbose_name='Год выпуска'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание произведения'
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория произведения'
    )

    def check_year_value(self):
        year = self.year
        if year is not None and year > timezone.now().year:
            raise ValidationError(
                {'year': 'Год не может быть больше текущего.'}
            )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('name',)
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'year'],
                name='unique_name_year'
            )
        ]

    def __str__(self):
        return self.name


class Review(ModelPubDate):
    """Модель Review (отзыв)"""
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    score = models.PositiveSmallIntegerField(
        validators=(
            MinValueValidator(1, message='Минимальное значение: 1'),
            MaxValueValidator(10, message='Максимальное значение: 10')
        ),
=======

from api.constants import SYMBOLS_QUANTITY
from api_yamdb.settings import MAX_LEN_EMAIL, MAX_LEN_ROLE, MAX_LEN_USERNAME
from reviews.basemodel import BaseModel


class User(AbstractUser):
    """Модель User (пользователь)"""

    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'

    ROLE_CHOICES = [
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (USER, 'Пользователь'),
    ]
    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        unique=True,
        verbose_name='Имя пользователя',
        validators=[RegexValidator(
            r'^[\w-]+$', 'Недопустимый символ.'
        )],
    )
    email = models.EmailField(
        max_length=MAX_LEN_EMAIL,
        unique=True,
        verbose_name='Адрес электронной почты'
    )
    bio = models.TextField(
        blank=True,
        null=True,
        verbose_name='О себе'
    )
    role = models.CharField(
        max_length=MAX_LEN_ROLE,
        choices=ROLE_CHOICES,
        default=USER,
        verbose_name='Роль',
    )

    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)
        constraints = [
            models.CheckConstraint(
                name='cant_use_me_username',
                check=~models.Q(username='me'),
            ),
        ]

    def __str__(self):
        return self.username[:SYMBOLS_QUANTITY]

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR


class Genre(BaseModel):
    """Модель Genre (жанр)"""

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)

    def __str__(self):
        return f'Жанр: {self.name[:SYMBOLS_QUANTITY]}'


class Category(BaseModel):
    """Модель Category (категория)"""

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return f'Категория: {self.name[:SYMBOLS_QUANTITY]}'


class Title(models.Model):
    """Модель Title(произведение)"""
    name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Название произведения'
    )
    year = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        verbose_name='Год выпуска'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание произведения'
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория произведения'
    )

    @property
    def rating(self):
        avg_rating = self.reviews.aggregate(Avg('score'))['score__avg']
        if avg_rating is not None:
            return round(avg_rating, 2)
        return None

    def check_year_value(self):
        year = self.year
        if year is not None and year > timezone.now().year:
            raise ValidationError(
                {'year': 'Год не может быть больше текущего.'}
            )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('name',)
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'year'],
                name='unique_name_year'
            )
        ]

    def __str__(self):
        return self.name


class Review(models.Model):
    """Модель Review (отзыв)"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор отзыва',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    text = models.TextField(
        verbose_name='Текст отзыва'
    )
    score = models.PositiveSmallIntegerField(
        validators=(
            MinValueValidator(1, message='Минимальное значение: 1'),
            MaxValueValidator(10, message='Максимальное значение: 10')
        ),
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления'
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        unique_together = ['author', 'title']
<<<<<<< HEAD
=======
        ordering = ('title',)
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed

    def __str__(self):
        return self.text


<<<<<<< HEAD
class Comment(ModelPubDate):
    """Модель Comment (комментарий)"""
=======
class Comment(models.Model):
    """Модель Comment (комментарий)"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв на произведение'
    )
<<<<<<< HEAD
=======
    text = models.TextField(
        verbose_name='Текст комментарция'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления'
    )
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['pub_date']
<<<<<<< HEAD
=======

    def __str__(self):
        return self.text
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
