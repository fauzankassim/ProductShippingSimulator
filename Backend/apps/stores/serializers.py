from .models import Product, Transaction
from rest_framework import serializers

class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["id", "merchant", "title", "price", "created_at"]
        read_only_fields = ["merchant", "created_at"]


class TransactionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ["id", "product", "customer", "created_at"]
        read_only_fields = [ "customer", "created_at"]