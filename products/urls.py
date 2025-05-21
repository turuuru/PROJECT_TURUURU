from django.urls import path
from .views import custom_logout  # если используется
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('smartphones/', views.smartphones, name='smartphones'),
    path('support/', views.support, name='support'),
    path('about/', views.about, name='about'),
    path('add-to-cart/<int:phone_id>/', views.add_to_cart, name='add_to_cart'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
