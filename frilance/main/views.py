from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

def main(request):
    return render(request, "main/index.html")


def login_views(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile:profile')

    return render(request, 'registration/login.html')


