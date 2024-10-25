from django.contrib.auth.models import User
from django.db import models

# from phonenumber_field.modelfields import PhoneNumberField


# def profile_avatar_directory_path(instance: "Profile" ,filename: str) -> str:
#     return f"profile/profile_{instance.pk}/avatar/{filename}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    # phone = PhoneNumberField()
    delivery_address = models.CharField(max_length=250, blank=False)
    activate = models.BooleanField(default=True)
    # bio = models.TextField(max_length=500, blank=True)
    # agreement_accepted = models.BooleanField(default=False)
    # avatar = models.ImageField(null=True, upload_to=profile_avatar_directory_path, blank=True)