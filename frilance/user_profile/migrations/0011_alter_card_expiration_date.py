# Generated by Django 4.2.11 on 2024-03-20 20:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0010_card_balance_alter_card_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2034, 3, 18, 20, 15, 0, 196751, tzinfo=datetime.timezone.utc)),
        ),
    ]
