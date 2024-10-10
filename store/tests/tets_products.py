"""
TODO
        []  create =post
        []  update = put
        []  partial update =patch   
        []  get list =get
        []  retrieve = get+ id  
"""

import pytest
from model_bakery import baker


@pytest.mark.django_db
class TestCrateProduct:
    def test_if_user_is_anonymous_return_401(self, api_client):
        collection = baker.make("store.collection")
        data = {
            "title": "test product",
            "price": 100000,
            "inventory": 200,
            "collection": collection,
            "imsages": [{"image": "http://example.com"}],
        }
