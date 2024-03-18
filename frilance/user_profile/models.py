from datetime import timedelta
from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import random
from django.db.models.signals import post_save
from django.dispatch import receiver

class Account(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    image = models.ImageField(upload_to="user_images", blank = True)

    phone_number = PhoneNumberField()

    birthday = models.DateField(auto_now=False,
                                auto_now_add=False)
    
    address = models.TextField(help_text = 'E.x.: 551 Swanston Street, Melbourne')

    def __str__(self):
        return self.user.username
    
class Card(models.Model):
    CARD_TYPES = (
        ('P', 'Personal'),
        ('C', 'Commercial'),
    )

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    
    
    
    card_number =  models.CharField(max_length=16,
                                    unique=True,
                                    blank = True,
                                    help_text = "THE FIELD IS FILLED IN AUTOMATICALLY. LEAVE IT EMPTY")

    card_type = models.CharField(max_length=1,
                                 choices=CARD_TYPES,
                                 default = "P")
    
    creation_date = models.DateTimeField(auto_now_add=True)

    expiration_date = models.DateTimeField(default = timezone.now()+timedelta(days=365*10))
    
    balance = models.DecimalField(max_digits=10,
                                  decimal_places=2,
                                  default = 100)





    def __str__(self):
        return f'{self.card_number} ({self.user.username})'
    
    def save(self, *args, **kwargs):
        if not self.card_number:
            while True:
                card_number = ''.join(str(random.randint(0, 9)) for _ in range(16))
                if not Card.objects.filter(card_number=card_number).exists():
                    self.card_number = card_number
                    break
        super().save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_user_card(sender, instance, created, **kwargs):
    if created:
        Card.objects.create(user=instance)