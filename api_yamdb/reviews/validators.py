from django.core.exceptions import ValidationError
from django.utils import timezone


def creation_year_validator(value):
    if not (0 < value <= timezone.now().year):
        raise ValidationError(
            'Год создания не может быть больше текущего.'
        )