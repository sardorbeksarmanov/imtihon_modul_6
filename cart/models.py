from django.db import models
from shop.models import Shop


class Cart(models.Model):
    product = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cart/')
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.title} - {self.quantity}'

    @property
    def total_price(self):
        return self.product.price * self.quantity
