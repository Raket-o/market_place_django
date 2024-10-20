from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = "id", "name"

    name = models.CharField(max_length=50, blank=False, unique=True)

    def __repr__(self):
        # return self.__repr__()
        return self.name

    def __str__(self):
        return self.name


class Group(models.Model):
    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"
        ordering = "id", "name"

    name = models.CharField(max_length=50, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="names")

    # def __repr__(self):
    #     return self.__repr__()
    #     return f"{self.category},{self.name}"

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = "id", "name"

    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(null=False, blank=True)
    # price = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    price = models.DecimalField(null=False, max_digits=8, decimal_places=2, blank=False)
    discount = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(default=0)
    archived = models.BooleanField(default=False)
    # group = models.ManyToManyField(Group, on_delete=models.CASCADE, related_name="name")
    # group = models.ManyToManyField(Group, related_name="name")
    group = models.ManyToManyField(Group)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # created_by = models.CharField(default=User)

    # def __repr__(self):
    #     return self.name

    def __str__(self):
        return self.name
