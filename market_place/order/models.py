from django.contrib.auth.models import User
from django.db import models


class Status(models.Model):
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    name = models.CharField(max_length=20, null=False, blank=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class CustomProductClass:
    def __init__(self, id, name, price, size, color, photo):
        self.id = id
        self.name = name
        self.price = price
        self.size = size
        self.color = color
        self.photo = photo

    def __str__(self):
        return f"{self.id}, {self.name}, {self.price}, {self.size}, {self.color}, {self.photo}"


class Order(models.Model):
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    products = models.TextField(null=False, blank=True)
    total_price = models.DecimalField(null=False, max_digits=8, decimal_places=2, blank=False)

    def __str__(self):
        return f"Order(id={self.pk}, user={self.user}, status={self.status.name})"

    def __repr__(self):
        return str(self.__dict__)
