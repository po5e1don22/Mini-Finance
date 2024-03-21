from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user_profile.models import Card
from decimal import Decimal
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Transaction
from django.core.paginator import Paginator

@login_required
def wallet(request):
    transactions_list = Transaction.objects.filter(card__user=request.user)
    paginator = Paginator(transactions_list, 10)  
    page_number = request.GET.get('page')
    transactions = paginator.get_page(page_number)
    return render(request, 'transactions/wallet.html', {'transactions': transactions})

@login_required
def transation_detail(request):
    return render(request, "transactions/transation-detail.html")

@login_required
def transfer(request):
    users = User.objects.all()
    return render(request, 'transactions/transfer.html', {'users': users})

@login_required
def transfer(request):
    if request.method == 'POST':
        sender_card = Card.objects.get(user=request.user)
        recipient_id = request.POST.get('userSelect')
        amount = Decimal(request.POST.get('transferAmount'))
        recipient_card = get_object_or_404(Card, user_id=recipient_id)

        try:
            Transaction.create_transfer(sender_card, recipient_card, amount)
        except ValueError:
            # Обрабатываем ошибку недостаточного баланса
            return HttpResponse("Insufficient balance")

        return HttpResponseRedirect('/')  
    else:
        users = User.objects.all()
        return render(request, 'transactions/transfer.html', {'users': users})

