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
        return f'Категория: {self.name[:SYMBOLS_QUANTITY]}'