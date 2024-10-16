from django.contrib import admin

from .models import Category, Group, Product


admin.site.register([Category, Group, Product])
# admin.site.register(Category)
# admin.site.register(Group)
# admin.site.register(Product)
