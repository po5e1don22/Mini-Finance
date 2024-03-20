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
    @transaction.atomic
    def transfer(self, amount, recipient_card):

        # Block cards for the current transaction
        cards = Card.objects.select_for_update().filter(id__in=[self.id, recipient_card.id])

        if self.balance < amount:
            raise ValueError("Insufficient funds for the transfer")
        self.balance -= amount
        recipient_card.balance += amount
        self.save()
        recipient_card.save()