# Generated by Django 4.1.5 on 2023-01-27 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0004_alter_transaction_card_alter_transaction_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="date",
            field=models.CharField(max_length=10),
        ),
    ]
