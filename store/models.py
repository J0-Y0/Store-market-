from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    collection = models.ManyToManyField("Collection", on_delete=models.PROTECT)


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255, unique=True)
    birthday = models.DateField(null=True, blank=True)

    membership_choices = [
        ("B", "bronze"),
        ("S", "Sliver"),
        ("G", "Gold"),
    ]
    membership = models.CharField(choices=membership_choices, max_length=1, default="B")


class Address(models.Model):
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Collection(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


# Represents each individual item in an order. While an Order contains overall details,
class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()


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
    # add to cart option is available to both registered and non registered user
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()


class Promotion(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, on_delete=models.PROTECT)
    discount_value = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
