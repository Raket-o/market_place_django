from django.contrib.auth.models import User
from django.core.management import BaseCommand

from authorization.models import Profile

from env_data import login_superuser


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create superuser")
        user = User.objects.filter(username=login_superuser)
        if not user:
            superuser = User(
                password="pbkdf2_sha256$720000$VPZHdMONCcHSJljzWYws8S$/ounvLrr0Au7AwU23u0XN3ot5+GQnnDjjARhf0Oywts=",
                is_superuser=True,
                username=login_superuser,
                is_staff=True,
                is_active=True
            )
            superuser.save()
            self.stdout.write(self.style.SUCCESS("Superuser created"))

            profile = Profile(user_id=superuser.id)
            profile.save()
            self.stdout.write(self.style.SUCCESS("Superuser Profile created"))
        else:
            self.stdout.write(self.style.SUCCESS("Superuser already exists"))
