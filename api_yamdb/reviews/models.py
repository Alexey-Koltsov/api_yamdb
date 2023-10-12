from django.db import models


class Genre(models.Model):
    """Модель жанра."""
    
    name = models.CharField(
        max_length=256,
        verbose_name='Название'
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
        return self.name[:20]


class Category(models.Model):
    """Модель категорий."""

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
        return self.name[:20]


class Title(models.Model):
    """Модель произведений."""
    
    name = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    year = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='Год выпуска'
    )
    rating = models.IntegerField(
        null=True,
        verbose_name='Рейтинг на основе отзывов'
    )
    description = models.TextField(
        blank=True, 
        null=True, 
        verbose_name='Описание'
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
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name[:20]
