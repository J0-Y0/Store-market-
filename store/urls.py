from django.urls import path, include
from .views import *
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register("collections", CollectionViewSet)
router.register("products", ProductViewSet, basename="products")
router.register("carts", CartVewSet, basename="carts")
router.register("customers", CustomerViewSet, basename="customers")

# Nested router for comments
product_router = routers.NestedDefaultRouter(router, "products", lookup="product")
product_router.register("comments", ProductCommentViewSet, basename="product-comments")
# Nested router for carts
cart_router = routers.NestedDefaultRouter(router, "carts", lookup="cart")
cart_router.register("items", CartItemViewSet, basename="cart-items")
urlpatterns = [
    path("", include(router.urls)),
    path("", include(product_router.urls)),
    path("", include(cart_router.urls)),
]
