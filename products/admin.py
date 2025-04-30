from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'memory', 'price')
    search_fields = ('name', 'brand')
    list_filter = ('brand', 'memory')
