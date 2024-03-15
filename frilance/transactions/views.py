from django.shortcuts import render


def wallet(request):
    return render(request, "transactions/wallet.html")

def transation_detail(request):
    return render(request, "transactions/transation-detail.html")

