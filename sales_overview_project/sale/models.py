import datetime

from django.db import models
from django.contrib.auth.models import User


class Delivery(models.Model):
    delivery_type = models.CharField(max_length=150)


class Payment(models.Model):
    payment_type = models.CharField(max_length=150)


class Shop(models.Model):
    shop_name = models.CharField(max_length=200)
    city = models.CharField(max_length=150)


class Employee(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150)
    passport_number = models.CharField(max_length=150)
    birthdate = models.DateTimeField(default=datetime.datetime.now())


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    cost = models.FloatField
    cost_price = models.FloatField


class Sale(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='deliveries')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='payments')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shops')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employees')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    product = models.ForeignKey
