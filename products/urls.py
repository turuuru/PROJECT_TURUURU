from django.urls import path
from . import views

urlpatterns = [
    path('phones/', views.phone_list, name='phone_list'),
]
