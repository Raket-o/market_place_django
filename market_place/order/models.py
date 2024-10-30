from django.contrib.auth.models import User
from django.db import models

from shop.models import Product


class Status(models.Model):
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    name = models.CharField(max_length=20, null=False, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    promocode = models.CharField(max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ManyToManyField(Status, related_name="orders")
    products = models.ManyToManyField(Product, related_name="orders")

    def __str__(self):
        return f"Order(id={self.pk}, user={self.user})"
