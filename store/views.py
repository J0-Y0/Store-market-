from django.shortcuts import render
from .models import Product, OrderItem, Customer, Order
from django.db.models import Q, F, Value
from django.db.models.aggregates import Count, Sum
from django.db import transaction


def test(request):
    product = OrderItem.objects.filter(pk__in=(1, 2, 3)).delete()
    return render(request, "test.html")
