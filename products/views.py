from django.shortcuts import render
from .models import Phone

def phone_list(request):
    phones = Phone.objects.all()  # Получаем все телефоны из базы данных
    return render(request, 'products/phone_list.html', {'phones': phones})