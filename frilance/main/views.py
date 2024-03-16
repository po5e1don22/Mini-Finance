from django.shortcuts import render

def main(request):
    return render(request, "main/index.html")


def login(request):
    return render(request, 'registration/login.html')

# Create your views here.
