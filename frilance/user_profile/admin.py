from django.contrib import admin
from user_profile.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from user_profile import models

class AccountInLine(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'

class CustomUserAdmin (UserAdmin):
    inlines = (AccountInLine,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(models.Card)
class AdminCard(admin.ModelAdmin):
    list_display = [
        'user',
        'card_number',
        'card_type',
    ]