from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify


class story(models.Model):
    title = models.CharField(max_length=100)
    story = models.TextField(blank=True)
    createdTime = models.DateTimeField(default=timezone.now)
    image = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id), slugify(self.title)])
