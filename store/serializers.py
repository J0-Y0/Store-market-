from decimal import Decimal
from django.db import transaction
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import Collection, Product, Cart, CartItem, Customer, Order, OrderItem


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "user", "birthday", "phone", "membership"]


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


class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ["id", "product_id", "quantity"]

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError(f"No product with the given id: {value} ")
        return value

    def save(self, **kwargs):
        cart_id = self.context["cart_pk"]
        product_id = self.validated_data["product_id"]
        quantity = self.validated_data["quantity"]
        cart_item = CartItem.objects.filter(
            cart_id=cart_id, product_id=product_id
        ).first()
        if cart_item is not None:
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item

        else:
            self.instance = CartItem.objects.create(
                cart_id=cart_id, **self.validated_data
            )

        return self.instance


class PatchCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["quantity"]


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField("calculate_total_price")

    class Meta:
        model = Cart
        fields = ["id", "items", "total_price"]

    def calculate_total_price(self, cart: Cart):
        return sum([item.quantity * item.product.price for item in cart.items.all()])


class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()

    class Meta:
        model = OrderItem
        fields = ["product", "unit_price", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "customer", "created_at", "payment_status", "items"]


class OrderCreateSerializer(serializers.Serializer):
    with transaction.atomic():
        cart_id = serializers.UUIDField()

        def validate_cart_id(self, value):
            if not Cart.objects.filter(pk=value).exists():
                raise serializers.ValidationError("Cart not found | Invalid cart Id")
            if CartItem.objects.filter(cart_id=value).count() == 0:
                raise serializers.ValidationError("Empty cart | No product to order")
            return value

        def save(self, **kwargs):
            customer = Customer.objects.get(user_id=self.context["user_id"])
            cart_id = self.validated_data["cart_id"]

            order = Order.objects.create(customer=customer)
            cart_items = CartItem.objects.select_related("product").filter(
                cart_id=cart_id
            )

            order_items = [
                OrderItem(
                    order=order,
                    product=item.product,
                    unit_price=item.product.price,
                    quantity=item.quantity,
                )
                for item in cart_items
            ]
            OrderItem.objects.bulk_create(order_items)
            Cart.objects.filter(pk=cart_id).delete()
            return order
