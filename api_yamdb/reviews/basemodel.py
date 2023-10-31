from django.db import models

from reviews.models import User

class ModelPubDate(models.Model):
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления')
    author = models.ForeignKey(
        User,
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
        return self.text