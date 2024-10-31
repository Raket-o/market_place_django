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


class Product:
    def __init__(self, name, size, color, photo):
        self.name = name,
        self.size = size,
        self.color = color,
        self.photo = photo,


class Order(models.Model):
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    # products = models.ManyToManyField(Product, related_name="orders")
    products = Product
    price = models.DecimalField(null=False, max_digits=8, decimal_places=2, blank=False)

    def __str__(self):
        return f"Order(id={self.pk}, user={self.user}, status={self.status.name})"
