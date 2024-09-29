from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductList.as_view(), name="products"),
    path("products/<int:pk>", views.ProductDetail.as_view(), name="productDetail"),
    path("collections/", views.CollectionList.as_view(), name="collections"),
    path(
        "collections/<int:pk>",
        views.CollectionDetail.as_view(),
        name="collectionDetail",
    ),
]
