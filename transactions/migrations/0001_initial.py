# Generated by Django 4.1.5 on 2023-01-27 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Débito", "Debito"),
                            ("Boleto", "Boleto"),
                            ("Financiamento", "Financiamento"),
                            ("Crédito", "Credito"),
                            ("Recebimento Empréstimo", "Emprestimo"),
                            ("Vendas", "Vendas"),
                            ("Recebimento TED", "Ted"),
                            ("Recebimento DOC", "Doc"),
                            ("Aluguel", "Aluguel"),
                        ],
                        max_length=25,
                    ),
                ),
                ("value", models.CharField(max_length=15)),
                ("cpf", models.CharField(max_length=11)),
                ("card", models.CharField(max_length=15)),
                ("date", models.DateField()),
                ("hour", models.TimeField()),
                ("shop_name", models.CharField(max_length=25)),
                ("shop_owner", models.CharField(max_length=15)),
            ],
        ),
    ]
