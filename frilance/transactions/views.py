from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def wallet(request):
    return render(request, "transactions/wallet.html")
@login_required
def transation_detail(request):
    return render(request, "transactions/transation-detail.html")

