from django.contrib.auth.models import AbstractUser
from django.db import models

import uuid


class User(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_legal = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
