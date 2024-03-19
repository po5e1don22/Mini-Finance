

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
import os
from django.conf import settings as django_settings

@login_required
def settings(request):
    return render(request, 'settings/setting.html')


def profile_update(request):
    if request.method == 'POST':
        username = request.POST.get('profile-name')
        email = request.POST.get('profile-email')
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