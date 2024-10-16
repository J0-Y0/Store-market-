from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # pass
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    REQUIRED_FIELDS = ["first_name", "last_name"]
    USERNAME_FIELD = "email"


# Custom fields can be added here if needed
