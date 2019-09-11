import uuid

from django.db import models


class Customer(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False
    )
    email_address = models.EmailField(max_length=254, unique=False)

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
