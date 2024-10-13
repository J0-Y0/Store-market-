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


def test_validate_file_size_raises_validation_error_when_file_size_exceeds_max(self):
    from django.core.files.uploadedfile import SimpleUploadedFile
    from django.core.exceptions import ValidationError

    # Create a file that exceeds the maximum size
    file_content = b"x" * (101 * 1024)  # 101 KB
    file = SimpleUploadedFile("test_file.txt", file_content)

    # Assert that ValidationError is raised
    with pytest.raises(ValidationError) as excinfo:
        validate_file_size(file)

    # Check the error message
    assert str(excinfo.value) == "File size should be less than 100 KB"
