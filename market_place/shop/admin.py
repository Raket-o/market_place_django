from django.contrib import admin

from .models import Category, Group, Product


admin.site.register([Category, Group, Product])
