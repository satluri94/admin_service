from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Food(models.Model):
    title = models.CharField(max_length=50, blank=False, default='')
    price = models.CharField(max_length=20, blank=False)

class Order(models.Model):
    id = models.CharField(max_length=50, blank=False, default='', primary_key=True)
    title = models.CharField(max_length=100, blank=False)

class Availability(models.Model):
    status = models.BooleanField(default=True)
    opening = models.CharField(max_length=10, blank=False)
    closing = models.CharField(max_length=10, blank=False)

class NewOrders(models.Model):
    id = models.CharField(max_length=50, blank=False, default='', primary_key=True)
    title = models.CharField(max_length=50, blank=False, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)