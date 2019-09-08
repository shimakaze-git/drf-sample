from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel


class Member(SoftDeletableModel, TimeStampedModel):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    birthday = models.DateField(null=True, default=None)


class Article(SoftDeletableModel, TimeStampedModel):
    STATUS_TYPE = (
        (0, '下書き'),
        (1, '公開中')
    )

    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS_TYPE)
    member = models.ForeignKey(
        Member,
        related_name='articles',
        on_delete=models.SET_NULL,
        null=True
    )
