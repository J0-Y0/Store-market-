from django.shortcuts import render
from .models import Product
from django.db.models import Q, F


def test(request):
    query_set = Product.objects.values("id", "title", "price", "collection__name")
    context = {"datas": list(query_set)}
    return render(request, "test.html", context)
