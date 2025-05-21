from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def support_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Здесь можно добавить отправку email
        send_mail(
            f"Сообщение от {name}",
            message,
            email,
            [settings.SUPPORT_EMAIL],  # Адрес, на который отправляется письмо
            fail_silently=False,
        )
        
        # Возвращаем сообщение об успешной отправке
        return render(request, 'support.html', {'message_sent': True})
    
    return render(request, 'support.html', {'message_sent': False})
