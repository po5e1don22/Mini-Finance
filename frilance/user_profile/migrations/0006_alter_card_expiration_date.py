# Generated by Django 4.2.11 on 2024-03-14 23:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_alter_card_card_number_alter_card_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2034, 3, 12, 23, 57, 17, 818927, tzinfo=datetime.timezone.utc)),
        ),
    ]
