from locust import HttpUser, between, task
import random


class UserBrowsWebsite(HttpUser):
    wait_time = between(1, 3)

    @task(4)
    def view_products(self):

        id = [1, 4, 5, 9, 11, 14, 15]
        collection_id = random.choice(id)
        self.client.get("/store/products/", name="products")
        self.client.get(
            f"/store/products/?collection_id={collection_id}",
            name="products/:collection",
        )

    @task(3)
    def view_product(self):

        id = random.randint(1, 1000)
        self.client.get(f"/store/products/{id}", name="products/:id")

    @task(1)
    def add_to_cart(self):

        product_id = random.randint(1, 1000)
        self.client.post(
            f"/store/carts/{self.cart_id}/items/",
            json={"product_id": product_id, "quantity": 5},
            name="carts/items",
        )

    @task(1)
    def view_carts(self):
        self.client.get(f"/store/carts/{self.cart_id}/items/", name="cart:id/items")

    def on_start(self):

        response = self.client.post(f"/store/carts/", name="cart:initial")
        data = response.json()
        self.cart_id = data["id"]
