from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

from reviews.models import User


def send_confirmation_code(user: User):
    """Отправка кода подтверждения."""

    confirmation_code = default_token_generator.make_token(user)
    message = f'Ваш код подтверждения: {confirmation_code}'

    send_mail(
        'Ваш код подтверждения',
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
<<<<<<< HEAD
    )
=======
    )
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
