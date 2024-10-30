import re

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


def validate_phone_number(value):
    pattern = r'^\+?\d+$'
    if not re.match(pattern, value):
        raise ValidationError('Неверный формат телефонного номера.')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, validators=[validate_phone_number])
    delivery_address = models.CharField(max_length=250, blank=False)
    activate = models.BooleanField(default=True)

    def __str__(self):
        return f"Profile(id={self.pk}, user={self.user})"
