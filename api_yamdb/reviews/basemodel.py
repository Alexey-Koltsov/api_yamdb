from django.db import models

from api_yamdb.settings import MAX_LEN_NAME, MAX_LEN_SLUG


class BaseModel(models.Model):
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
