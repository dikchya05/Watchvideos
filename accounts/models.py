from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('user', 'Normal User'),
    )
    role = models.CharField(max_length=10, choices=USER_ROLES, default='user')

    # Fix field clashes by defining related names
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",
        blank=True
    )
