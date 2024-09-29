from decimal import Decimal
from rest_framework import serializers
from .models import Collection, Product


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = "__all__"  # Or specify needed fields


class ProductSerializer(serializers.ModelSerializer):
    # collection = CollectionSerializer()  # Nested collection serializer
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    class Meta:
        model = Product
        fields = ["id", "title", "price", "price_with_tax", "inventory", "collection"]

    # Custom method to calculate tax
    def calculate_tax(self, product: Product):
        if product.price is None:
            return None
        return product.price * Decimal(1.1)

    def create(self, validated_data):
        product = Product(**validated_data)
        product.description = "yosef"
        product.save()
        return product
