from django.shortcuts import render
from .models import Product
from django.db.models import Q


def test(request):
    query_set = Product.objects.filter(~Q(id__gt=50) | Q(price__lt=100))
    context = {"datas": list(query_set)}
    return render(request, "test.html", context)
