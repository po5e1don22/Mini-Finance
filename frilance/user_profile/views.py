from django.shortcuts import render

import user_profile

def profile(request):
    return render(request, 'user_profile/profile.html')

# Create your views here.
