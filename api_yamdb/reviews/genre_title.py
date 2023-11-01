from django.db import models
<<<<<<< HEAD

=======
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
from reviews.models import Genre, Title


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
