from django.contrib import admin
from django.urls import path, include
from products import views  # 👈 импортируем views
from products.views import phone_list

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Главная страница и другие разделы
    path('', views.index, name='home'),
    path('smartphones/', views.smartphones, name='smartphones'),
    path('accessories/', views.accessories, name='accessories'),
    path('support/', views.support, name='support'),
    path('about/', views.about, name='about'),

    # Телефоны, корзина и заказы
    path('phones/', phone_list, name='phone_list_phones'),
    path('carts/', include('carts.urls')),
    path('orders/', include('orders.urls')),
]
