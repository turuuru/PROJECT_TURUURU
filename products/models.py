from django.db import models

class Product(models.Model):
    BRAND_CHOICES = [
        ('apple', 'Apple'),
        ('samsung', 'Samsung'),
        ('xiaomi', 'Xiaomi'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    memory = models.PositiveIntegerField(help_text="Memory in GB")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
