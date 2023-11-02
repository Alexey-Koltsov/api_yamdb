from django.db import models

from api.constants import SYMBOLS_QUANTITY
from api_yamdb.settings import MAX_LEN_NAME, MAX_LEN_SLUG


class NameSlugBaseModel(models.Model):
    name = models.CharField(
        max_length=MAX_LEN_NAME,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=MAX_LEN_SLUG,
        unique=True,
        verbose_name='Slug'
    )

    class Meta:
        abstract = True
        ordering = ('name',)

    def __str__(self):
        return f'{self.name[:SYMBOLS_QUANTITY]}'


class ModelPubDate(models.Model):
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления')
    author = models.ForeignKey(
        'reviews.User',
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related",
        verbose_name='Автор')
    text = models.TextField(
        verbose_name='Текст'
    )

    class Meta:
        abstract = True
        ordering = ('title',)

    def __str__(self):
        return self.text[:SYMBOLS_QUANTITY]