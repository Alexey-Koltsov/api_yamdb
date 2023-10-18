from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models


class RoleEnum(Enum):
    user: str = 'user'
    moderator: str = 'moderator'
    admin: str = 'admin'


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField('Биография', blank=True)
    role = models.CharField(
        'Роль',
        choices=[(choice, choice.value) for choice in RoleEnum],
        default=RoleEnum.user.value,
        max_length=9,
    )
    confirmation_code = models.CharField(
        max_length=16,
        unique=True,
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='username_can_not_be_me',
                check=~models.Q(username='me'),
            ),
        ]

    def __str__(self):
        return f'Пользователь: {self.username}'
