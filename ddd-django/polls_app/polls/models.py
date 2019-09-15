from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.contrib import admin

from model_utils.models import TimeStampedModel
import datetime


class Question(TimeStampedModel):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(TimeStampedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class UserChoice(TimeStampedModel):
    choice = models.ForeignKey(Choice, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# admin.site.register(Question)
# admin.site.register(Choice)
