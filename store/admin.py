from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.utils.html import format_html, urlencode
from django.contrib.contenttypes.admin import GenericTabularInline
from django.urls import reverse
from .models import *
from common.models import *


from django.db.models import Count, F


# custom filter
class InventoryStatusFilter(admin.SimpleListFilter):
    title = "by Inventory status"
    parameter_name = "inventory"

    def lookups(self, request, model_admin):
        return [
            (">500", "Enough"),
            (">50", "Low"),
            ("<=50", "Very Low"),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == ">500":
            return queryset.filter(inventory__gt=100)
        elif self.value() == ">50":
            return queryset.filter(inventory__gt=50, inventory__lte=100)
        elif self.value() == "<=50":
            return queryset.filter(inventory__lte=50)


# custom action
@admin.action(description="Clear inventory")
def clear_inventory(self, request, queryset):
    updated_count = queryset.update(inventory=0)
    self.message_user(
        request, f"inventory of {updated_count} products cleared successfully"
    )


# inline child list
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    autocomplete_fields = ["product"]
    extra = 0
    # allowed maximum  amd minimum order item per order

    min_num = 1
    max_num = 4


class CommentInline(GenericTabularInline):
    model = Comment
    extra = 1  # Number of empty comments to display for adding new ones


class LikeInline(GenericTabularInline):
    model = Like
    extra = 1


class ContentTagInline(GenericTabularInline):
    model = ContentTag
    extra = 1


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email",
        "phone",
        "order_count",
        "membership",
    ]
    search_fields = [
        "first_name__istartswith",
    ]
    list_filter = ["membership"]
    list_editable = ["membership"]
    list_per_page = 10

    ordering = ["first_name", "last_name"]

    @admin.display(ordering="order_count")
    def order_count(self, customer):
        url = (
            reverse("admin:store_order_changelist")
            + "?"
            + urlencode({"customer__id__exact": customer.id})
        )

        return format_html(f"<a href = {url}>{customer.order_count}</a>")

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(order_count=Count("order"))


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # action
    actions = [clear_inventory]

    list_display = [
        "title",
        "collection__title",
        "price",
        "last_update",
        "inventory_status",
    ]
    list_select_related = ["collection"]

    list_filter = ["collection__title", "last_update", InventoryStatusFilter]
    list_editable = ["price"]
    list_per_page = 10
    search_fields = ["title", "description"]

    ordering = ["title"]

    inlines = [CommentInline, ContentTagInline]

    autocomplete_fields = ["collection"]
    prepopulated_fields = {"description": ["title"]}

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory > 100:
            return f"Enough {product.inventory}"

        elif product.inventory > 50:
            return f"low {product.inventory}"
        return f"Very Low {product.inventory}"


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


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "customer", "items_count", "payment_status"]
    list_filter = ["payment_status", "created_at"]
    search_fields = ["customer__first_name", "customer__last_name", "customer__email"]
    ordering = ["id"]
    autocomplete_fields = ["customer"]

    list_select_related = ["customer"]
    list_per_page = 15

    inlines = [OrderItemInline]

    @admin.display(ordering="items_count")
    def items_count(self, order):
        url = (
            reverse("admin:store_orderitem_changelist")
            + "?"
            + urlencode({"order__id__exact": order.id})
        )
        return format_html(f"<a href = {url}>{order.items_count}</a>")

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(items_count=Count("orderitem"))


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "order",
        "product__title",
        "unit_price",
        "quantity",
        "total_price",
    ]
    search_fields = [
        "order__customer__first_name",
        "order__id",
        "product__title",
    ]
    autocomplete_fields = ["product"]

    ordering = ["id"]

    @admin.display(ordering="total_price")
    def total_price(self, orderitem):
        return orderitem.total_price

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return (
            super()
            .get_queryset(request)
            .annotate(total_price=F("quantity") * F("unit_price"))
        )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at"]
    search_fields = ["id"]
    ordering = ["created_at"]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ["cart", "product", "quantity"]
    search_fields = ["cart__id", "product__title"]
    ordering = ["cart"]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ["customer", "region", "city"]
    search_fields = ["customer__first_name", "customer__last_name", "region", "city"]
    ordering = ["customer", "region", "city"]


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ["title", "discount_value", "start_date", "end_date"]
    search_fields = ["title"]
    ordering = ["start_date"]
