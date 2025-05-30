from django.db import models


class Organization(models.Model):
    """Модель организации."""

    inn = models.CharField(max_length=12, unique=True)
    balance = models.BigIntegerField(default=0)

    def __str__(self):
        return self.inn


class Payment(models.Model):
    """Модель платежа."""

    operation_id = models.UUIDField(unique=True)
    amount = models.BigIntegerField()
    payer = models.ForeignKey(Organization, on_delete=models.CASCADE,
                              related_name='payments')
    document_number = models.CharField(max_length=64)
    document_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.operation_id}"
