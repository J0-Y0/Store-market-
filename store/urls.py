from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.productList, name="products"),
    path("products/<int:id>", views.productDetail, name="productDetail"),
]
