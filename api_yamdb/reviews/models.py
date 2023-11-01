from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models
from django.utils import timezone

from api.constants import SYMBOLS_QUANTITY
from api_yamdb.settings import (
    MAX_LEN_EMAIL,
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
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        unique_together = ['author', 'title']


class Comment(ModelPubDate):
    """Модель Comment (комментарий)"""
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв на произведение'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['pub_date']


class GenreTitle(models.Model):
    """Модель связи Genre и Title"""

    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f'{self.title} {self.genre}'
