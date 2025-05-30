from rest_framework import serializers
from core.models import Organization

class OrganizationBalanceSerializer(serializers.ModelSerializer):
    """Баланс организации."""

    class Meta:
        model = Organization
        fields = ('inn', 'balance')

class OrganizationCreateSerializer(serializers.ModelSerializer):
    """Создание организации."""

    class Meta:
        model = Organization
        fields = ('inn',)

class BankWebhookSerializer(serializers.Serializer):
    """Банковский вебхук."""

    operation_id = serializers.UUIDField()
    amount = serializers.IntegerField()
    payer_inn = serializers.CharField(max_length=12)
    document_number = serializers.CharField()
    document_date = serializers.DateTimeField()
