from os import name
from sqlite3 import Timestamp
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField
from numpy import product

# Create your models here.
class User(AbstractUser):
    following = models.ManyToManyField("self",symmetrical=False, related_name="followers")
    pass

class Product(models.Model):
    name = models.CharField(max_length=64)
    buying_price =  models.DecimalField(max_digits=7, decimal_places=2)
    selling_price =  models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self) -> str:
        return f"{self.name}"

class Client(models.Model):
    name = models.CharField(max_length=64)
    contact = models.CharField(max_length=12)
    timestamp = models.DateTimeField(auto_now_add=True)
    purchases = models.ManyToManyField(Product, blank=True)
    def __str__(self) -> str:
        return f"{self.name}-{self.contact}"

class Activity(models.Model):
    types = [
        ('deposit','Deposit'),
        ('withdraw', 'Withdraw'),
        ('purchase', 'purchase'),
        ('refund','Refund'),
        ('custom', 'Custom')
    ]
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=160)
    participants = models.ManyToManyField(User,blank=True)
    investement = models.DecimalField(max_digits=12, decimal_places=3)
    type = models.CharField(max_length=64, choices=types, default="custom")
    gain = models.DecimalField(max_digits=12, decimal_places=3)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}"

class Project(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=160)
    host = models.ForeignKey(User, on_delete=models.CASCADE,related_name='hosts')
    members = models.ManyToManyField(User, related_name="in_projects")
    activity = models.ManyToManyField(Activity, blank=True, related_name="project")
    timestamp = models.DateTimeField(auto_now_add=True)
    revenue = models.DecimalField(max_digits=12, decimal_places=3)
    income = models.DecimalField(max_digits=12, decimal_places=3, blank=True)
    products = models.ManyToManyField(Product, blank=True, related_name="product_projects")
    clients = models.ManyToManyField(Client, blank=True, related_name="client_projects")

    def __str__(self) -> str:
        return f"{self.name}:{self.id}"

