from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import (MaxValueValidator, MinValueValidator, RegexValidator)
from django.db import models
from django.db.models import Avg
from django.utils import timezone

from reviews.basemodel import BaseModel
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
    bio = models.TextField(
        blank=True,
        null=True,
        verbose_name='О себе'
    )
    role = models.CharField(
        max_length=12,
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
        ordering = ['id']

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
        ordering = ['name']


class Category(BaseModel):
    """Модель Category (категория)"""

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Title(models.Model):
    """Модель Title(произведение)"""
    name = models.CharField(
        max_length=256,
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

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'year'],
                name='unique_name_year'
            )
        ]
        ordering = ['name']

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
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        unique_together = ['author', 'title']
        ordering = ['title']

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Модель Comment (комментарий)"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв на произведение'
    )
    text = models.TextField(
        verbose_name='Текст комментарция'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['pub_date']

    def __str__(self):
        return self.text
