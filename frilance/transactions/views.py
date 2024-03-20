from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user_profile.models import Card
from decimal import Decimal
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Transaction

@login_required
def wallet(request):
    return render(request, "transactions/wallet.html")

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

        transaction = Transaction.objects.create(
        card=sender_card,
        description="money transfer",
        payment_type="transfer",
        amount=amount,
        balance_after_transaction=sender_card.balance,
        status='S'  
    )
        sender_card.transfer(amount, recipient_card)


        return HttpResponseRedirect('/')  
    else:
        users = User.objects.all()
        return render(request, 'transactions/transfer.html', {'users': users})

