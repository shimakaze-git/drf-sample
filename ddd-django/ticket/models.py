import uuid

from django.db import models


class Ticket(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False
    )
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    customer_uuid = models.UUIDField(
        blank=True, null=True, editable=True
    )
