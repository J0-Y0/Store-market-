from django.contrib import admin
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse
from .models import *

from django.db.models import Count


# Custom admin for Customer model
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone", "membership"]
    search_fields = ["first_name", "last_name", "email", "phone"]
    list_filter = ["membership"]
    list_editable = ["membership"]
    list_per_page = 10

    ordering = ["first_name", "last_name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "collection__title",
        "price",
        "last_update",
        "inventory_status",
    ]
    # list_select_related = ["collection"]

    list_filter = ["collection__title", "last_update"]
    list_editable = ["price"]
    list_per_page = 10
    search_fields = ["title", "description"]
    ordering = ["title"]

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory > 50:
            return "Enough"
        elif product.inventory > 25:
            return "low"
        return "Very Low"


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "product_count", "created_at"]
    list_editable = ["title"]
    search_fields = ["title"]
    ordering = ["pk"]

    @admin.display(ordering="product_count")
    def product_count(self, collection):
        # url = reverse("admin:app_model_page")
        url = (
            reverse("admin:store_product_changelist")
            + "?"
            + urlencode({"collection__title": collection.title})
        )
        return format_html(f'<a href = "{url}">{collection.product_count}</a>')

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(product_count=Count("product"))


# Custom admin for Order model
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "customer", "items_count", "payment_status"]
    list_filter = ["payment_status", "created_at"]
    search_fields = ["customer__first_name", "customer__last_name", "customer__email"]
    ordering = ["id"]

    list_select_related = ["customer"]
    list_per_page = 15

    @admin.display(ordering="items_count")
    def items_count(self, order):
        return order.items_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(items_count=Count("orderitem"))


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product__title", "unit_price", "quantity"]
    search_fields = [
        "order__customer__first_name",
        "order__customer__last_name",
        "product__title",
    ]
    list_filter = ["order__customer__first_name"]

    ordering = ["order"]


# Custom admin for Cart model
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at"]
    search_fields = ["id"]
    ordering = ["created_at"]


# Custom admin for CartItem model
class CartItemAdmin(admin.ModelAdmin):
    list_display = ["cart", "product", "quantity"]
    search_fields = ["cart__id", "product__title"]
    ordering = ["cart"]


# Custom admin for Address model
class AddressAdmin(admin.ModelAdmin):
    list_display = ["customer", "region", "city"]
    search_fields = ["customer__first_name", "customer__last_name", "region", "city"]
    ordering = ["customer", "region", "city"]


# Custom admin for Promotion model
class PromotionAdmin(admin.ModelAdmin):
    list_display = ["title", "discount_value", "start_date", "end_date"]
    search_fields = ["title"]
    ordering = ["start_date"]


# Register the models with the custom admin views
admin.site.register(Customer, CustomerAdmin)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Collection, CollectionAdmin)
admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Promotion, PromotionAdmin)
