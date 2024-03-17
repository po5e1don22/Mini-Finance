from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def FAQ(request):
    return render( request,'FAQ/help-center.html')

# Create your views here.
