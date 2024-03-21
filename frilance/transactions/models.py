from django.db import models, transaction
from django.contrib.auth.models import User
from django.utils import timezone
from user_profile.models import Card


class Transaction(models.Model):
    STATUS_CHOICES = (
        ('S', 'Successful'),
        ('D', 'Declined'),
        ('P', 'Pending'),
    )

    card = models.ForeignKey("user_profile.Card", on_delete=models.CASCADE)

    transaction_date = models.DateField(default=timezone.now)

    transaction_time = models.TimeField(default=timezone.now)

    description = models.CharField(max_length=255)

    payment_type = models.CharField(max_length=255)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    balance_after_transaction = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(max_length=1, choices = STATUS_CHOICES, default='P')


    #transaction system
    @staticmethod
    def create_transfer(sender_card, recipient_card, amount):
        if sender_card.balance >= amount:
            sender_card.balance -= amount
            recipient_card.balance += amount
            sender_card.save()
            recipient_card.save()

           
            sender_transaction = Transaction.objects.create(
                card=sender_card,
                description="Money transfer to user {}".format(recipient_card.user.username),
                payment_type="Transfer",
                amount=-amount,  
                balance_after_transaction=sender_card.balance,
                status='S'  
            )

            
            recipient_transaction = Transaction.objects.create(
                card=recipient_card,
                description="Money transfer from user {}".format(sender_card.user.username),
                payment_type="Transfer",
                amount=amount,  
                balance_after_transaction=recipient_card.balance,
                status='S'  
            )
        else:
            raise ValueError("Insufficient balance")