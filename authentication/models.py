from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    email = models.EmailField(unique=True)

    # Redefine groups and user_permissions with unique related_name
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Use a unique related name
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set",  # Use a unique related name
        blank=True,
        help_text="Specific permissions for this user.",
    )
