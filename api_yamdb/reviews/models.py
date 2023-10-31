from api.constants import SYMBOLS_QUANTITY
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models
from django.db.models import Avg
from django.utils import timezone

from reviews.basemodel import ModelPubDate

class User(AbstractUser):
    """Модель User (пользователь)"""

    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'

    ROLE_CHOICES = [
        (ADMIN, 'Administrator'),
        (MODERATOR, 'Moderator'),
        (USER, 'User'),
    ]
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Имя',
        validators=[RegexValidator(
            r'^[\w-]+$', 'Недопустимый символ.'
        )],
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Адрес электронной почты'
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Фамилия'
    )
    bio = models.TextField(
        blank=True,
        null=True,
        verbose_name='О себе'
    )
    role = models.CharField(
        max_length=150,
        choices=ROLE_CHOICES,
        default=USER
    )

    REQUIRED_FIELDS = ['email']

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='cant_use_me_username',
                check=~models.Q(username='me'),
            ),
        ]

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR


class Genre(models.Model):
    """Модель Genre (жанр)"""

    name = models.CharField(
        max_length=256,
        verbose_name='Название жанра'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Slug'
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f'Жанр: {self.name[:SYMBOLS_QUANTITY]}'


class Category(models.Model):
    """Модель Category (категория)"""

    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Slug'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'Категория: {self.name[:SYMBOLS_QUANTITY]}'


class Title(models.Model):
    """Модель Title(произведение)"""
    name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Название произведения'
    )
    year = models.PositiveIntegerField(
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
        blank=False,
        related_name='titles',
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='titles',
        verbose_name='Категория произведения'
    )

    @property
    def rating(self):
        avg_rating = self.reviews.aggregate(Avg('score'))['score__avg']
        if avg_rating is not None:
            return round(avg_rating, 2)
        return None


    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
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

    def __str__(self):
        return self.text


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
