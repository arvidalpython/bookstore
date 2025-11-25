from django.db import models
from django.contrib.auth.models import User
from product.models.product import Product
from django.conf import settings

class Order(models.Model):
    product = models.ManyToManyField(Product, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} - {self.product.name}"

    class Meta:
        app_label = 'order'