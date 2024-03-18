from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from user_profile.models import Account


@login_required
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


def logout_views(request):
    logout (request)

    return redirect('main:login')

def register_views(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            email = request.POST['email']
            phone_number = request.POST['phone_number']
            birthday = request.POST['birthday']
            address = request.POST['address']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 == password2:
                user = User.objects.create_user(username=username,
                                                      email=email,
                                                      password= password1)
                
                user.save()

                account = Account(user = user,
                                  phone_number=phone_number,
                                  birthday = birthday,
                                  address = address)
                account.save()
                login(request, user)
                print('Пользователь создан')
                return redirect('profile:profile')
            
            else:
                print('Пароли не совпадают')

        except MultiValueDictKeyError as e:
            print(f"Ошибка: {e}")

    else:
        return render(request, 'registration/registration.html',{})