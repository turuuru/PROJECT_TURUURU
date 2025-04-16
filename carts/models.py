from django.db import models
from django.contrib.auth.models import User
from products.models import Phone


class CartsItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
