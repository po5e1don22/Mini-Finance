from urllib import request
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
import os
from django.conf import settings as django_settings

@login_required
def settings(request):
    return render(request, 'settings/setting.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        username = request.POST.get('profile-name')

        email = request.POST.get('profile-email')\

        image = request.FILES.get('profile-image')

        if username:
            request.user.username = username

        if email:
            request.user.email = email

        if image:
            old_image_path = None

            if request.user.account.image and os.path.isfile(os.path.join(django_settings.MEDIA_ROOT, request.user.account.image.path)):
                old_image_path = os.path.join(django_settings.MEDIA_ROOT, request.user.account.image.path)

            request.user.account.image = image
            request.user.account.save()

            if old_image_path:
                os.remove(old_image_path)

        request.user.save()
        messages.success(request, 'Профиль успешно обновлен!')
        return redirect('settings:settings') 

    return render(request,'settings/setting.html')

@login_required()
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Ваш пароль был успешно обновлен!')
            return redirect('settings:settings')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибку.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'settings/setting.html', {
        'form': form
    })