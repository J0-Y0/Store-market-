from django.shortcuts import render
from .models import Product, OrderItem
from django.db.models import Q, F, Value
from django.db.models.aggregates import Count, Sum
from django.db import transaction


def test(request):
    product = Product.objects.get(id=1)

    # Access related comments
    comments = Product.comments.all()

    # Example: Print all comments
    for comment in comments:
        print(comment.comment_text)
        return render(request, "test.html")
