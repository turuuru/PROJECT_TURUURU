from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)

class Phone(models.Model):
    title = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='phones/')

