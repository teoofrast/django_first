from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField(default=0)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.id}'


class Buyer(models.Model):
    name = models.CharField(max_length=100, blank=False)
    nickname = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    password = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.nickname


class Cart(models.Model):
    buyer = models.OneToOneField(Buyer, on_delete=models.CASCADE, related_name='cart')
    products = models.ManyToManyField('Product', through='CartItem')

    def __str__(self):
        return f'Корзина юзера {self.buyer.nickname}'

    def display_products(self):
        return ', '.join([product.name for product in self.products.all()])
    display_products.short_description = 'Products'


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.product} - {self.cart.buyer}'
