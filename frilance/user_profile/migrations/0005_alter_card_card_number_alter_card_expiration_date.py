# Generated by Django 4.2.11 on 2024-03-14 23:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_alter_card_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_number',
            field=models.CharField(blank=True, help_text='THE FIELD IS FILLED IN AUTOMATICALLY. LEAVE IT EMPTY', max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2034, 3, 12, 23, 50, 27, 669240, tzinfo=datetime.timezone.utc)),
        ),
    ]
