from django.db import models

class TransactionType(models.TextChoices):
    DEBITO = "Débito"
    BOLETO = "Boleto"
    FINANCIAMENTO = "Financiamento"
    CREDITO = "Crédito"
    EMPRESTIMO = "Recebimento Empréstimo"
    VENDAS = "Vendas"
    TED = "Recebimento TED"
    DOC = "Recebimento DOC"
    ALUGUEL = "Aluguel"

class Transaction(models.Model):
    type = models.CharField(max_length=25, choices=TransactionType.choices)
    value = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    date = models.CharField(max_length=10)
    hour = models.CharField(max_length=10)
    shop_name = models.CharField(max_length=19)
    shop_owner = models.CharField(max_length=14)
