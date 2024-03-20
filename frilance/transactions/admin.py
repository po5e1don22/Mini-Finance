from django.contrib import admin
from transactions import models
# Register your models here.

@admin.register(models.Transaction)
class AdminTransaction(admin.ModelAdmin):
    list_display = [
        'card',
        'transaction_date',
        'transaction_time'
    ]