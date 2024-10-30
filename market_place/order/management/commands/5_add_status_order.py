from django.core.management import BaseCommand

from order.models import Status


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create status for order")

        status_list = (
            "Обработка",
            "Сборка",
            "Доставка",
            "Вручено",
        )

        for status in status_list:
            status, created = Status.objects.get_or_create(name=status)
            self.stdout.write(f"Created group {status.name}")

        self.stdout.write(self.style.SUCCESS("Status for order created"))
