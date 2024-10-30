from django.contrib import admin

from .models import Order, Status


admin.site.register([Order, Status])
