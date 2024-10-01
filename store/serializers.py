from decimal import Decimal
from rest_framework import serializers
from .models import Collection, Product, Cart, CartItem


class CollectionSerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)  # Annotated field

    class Meta:
        model = Collection
        fields = "__all__"


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


class SimpleProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "price",
        ]


class CartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField(method_name="calculate_total_price")
    product = SimpleProductSerializer()

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity", "total_price"]

    def calculate_total_price(self, cart_item: CartItem):
        if cart_item.product.price is None:
            return None
        return cart_item.product.price * cart_item.quantity


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField("calculate_total_price")

    class Meta:
        model = Cart
        fields = ["id", "items", "total_price"]

    def calculate_total_price(self, cart: Cart):
        return sum([item.quantity * item.product.price for item in cart.items.all()])
