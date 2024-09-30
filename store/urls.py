from django.urls import path, include
from .views import *
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register("collections", CollectionViewSet)
router.register("products", ProductViewSet, basename="products")
# Nested router for comments
product_router = routers.NestedDefaultRouter(router, "products", lookup="product")
product_router.register("comments", ProductCommentViewSet, basename="product-comments")
urlpatterns = [
    path("", include(router.urls)),
    path("", include(product_router.urls)),
]
