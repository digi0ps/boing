from django.db import models
from django.utils import timezone


class story(models.Model):
    title = models.CharField(max_length=100)
    story = models.TextField(blank=True)
    createdTime = models.DateTimeField(default=timezone.now)
