from .models import Product
from rest_framework import serializers

class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["id", "merchant", "title", "price", "created_at"]
        read_only_fields = ["merchant", "created_at"]

