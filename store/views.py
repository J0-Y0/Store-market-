from django.shortcuts import render
from .models import Product, OrderItem
from django.db.models import Q, F
from django.db.models.aggregates import Count


def test(request):
    query_set = Product.objects.aggregate(Count("collection"))

    # values("id", "title", "price", "collection__title")
    # query_set = Product.objects.values("collection").all()
    context = {"datas": (query_set)}
    return render(request, "test.html", context)
