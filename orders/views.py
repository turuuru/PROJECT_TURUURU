from django.shortcuts import render

def product_list(request):
    return render(request, 'products/smartphones.html')