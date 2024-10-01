from django.db import models
from django.utils import timezone

class Url(models.Model):
    original_url = models.URLField()
    short_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url
