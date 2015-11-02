from django.contrib import admin

from .models import OrderRow, Order, Item, Category

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderRow)
