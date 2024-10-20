from decimal import Decimal
from django.db import models
from uuid import uuid4
from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

from store.validators import validate_file_size


def product_image_path(instance, filename):
    return "products/{0}/{1}".format(instance.id, filename)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal(0), "price cant me negative"),
            MaxValueValidator(Decimal(10000), "unusual value"),
        ],
    )
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    collection = models.ForeignKey("Collection", on_delete=models.PROTECT)

    # comments = GenericRelation("common.Comment")  # Generic relation to Comment
    # likes = GenericRelation("common.Like")  # Generic relation to Like
    tags = GenericRelation("common.ContentTag")  # Generic relation to Tag

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-last_update"]


class FeedBack(models.Model):
    Product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="feedbacks"
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(
        upload_to=product_image_path,
        default="products/default_product.jpg",
        validators=[validate_file_size],
    )


class Customer(models.Model):

    phone = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    membership_choices = [
        ("B", "bronze"),
        ("S", "Sliver"),
        ("G", "Gold"),
    ]
    membership = models.CharField(choices=membership_choices, max_length=1, default="B")

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name } {self.user.last_name}"

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=["phone"],
    #             condition=models.Q(phone__isnull=False),
    #             name="unique_non_null_phone",
    #         )
    #     ]


class Address(models.Model):
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Collection(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Represents each individual item in an order. While an Order contains overall details,
class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.PROTECT, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.pk}"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_status_choice = [
        ("P", "Pending"),
        ("C", "Complete"),
        ("F", "Failed"),
    ]
    payment_status = models.CharField(
        choices=payment_status_choice, default="P", max_length=1
    )


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    # add to cart option is available to both registered and non registered user
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ("cart", "product")


class Promotion(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    products = models.ManyToManyField(Product)
    discount_value = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
