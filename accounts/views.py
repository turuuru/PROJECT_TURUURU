from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

def customLogout(request):
    logout(request)
    return redirect('home')

def support_view(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        full_message = f"Имя: {name}\nEmail: {email}\n\nСообщение:\n{message}"

        try:
            send_mail(
                subject='Новое сообщение в поддержку',
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            # Переход на страницу благодарности с сообщением об успешной отправке
            return render(request, 'support_thanks.html', {'success': True})
        except Exception as e:
            context['error'] = 'Ошибка при отправке сообщения. Попробуйте позже.'
    
    # Отображаем страницу поддержки с возможной ошибкой
    return render(request, 'support.html', context)
