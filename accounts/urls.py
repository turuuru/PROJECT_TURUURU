from django.urls import path
from .views import register, profile_view, customLogout, support_view

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile_view, name='profile'),
    path('logout/', customLogout, name='logout'),
    path('support/', support_view, name='support'),  # Добавлена поддержка
]
