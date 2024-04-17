from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
