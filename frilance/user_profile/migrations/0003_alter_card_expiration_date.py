# Generated by Django 4.2.11 on 2024-03-14 23:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_card_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2034, 3, 12, 23, 38, 36, 167731, tzinfo=datetime.timezone.utc)),
        ),
    ]