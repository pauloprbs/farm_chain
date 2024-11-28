from rest_framework import serializers

class TransactionSerializer(serializers.Serializer):
    sender = serializers.CharField(max_length=255)
    recipient = serializers.CharField(max_length=255)
    medicine = serializers.CharField(max_length=255)
    quantity = serializers.IntegerField()