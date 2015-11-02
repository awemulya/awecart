from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=254, null=True, blank=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Inventory Categories'


class Item(models.Model):
    name = models.CharField(max_length=253)
    company = models.CharField(max_length=253, null=True, blank=True)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Inventory Items'


class Order(models.Model):
    date = models.DateTimeField(null=True, blank=True)
    customer = models.ForeignKey(User)

    def __str__(self):
        return self.customer.first_name

    class meta:
        verbose_name_plural = u'Customer orders'


class OrderRow(models.Model):
    item = models.ForeignKey(Item)
    order = models.ForeignKey(Order, related_name='rows')

    def __str__(self):
        return self.order.customer.first_name+self.item.name