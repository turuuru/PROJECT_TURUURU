from django.db import models
from products.models import Product  # Импортируем модель Product

class Order(models.Model):
    customer_name = models.CharField(max_length=255, default='Не указано')  # Добавляем значение по умолчанию
    address = models.TextField(default='Не указано')
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, default=1)  # Задаем ID продукта по умолчанию (например, 1)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
