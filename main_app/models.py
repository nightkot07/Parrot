from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class News(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE,
                             blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    time = models.DateTimeField(blank=True, null=True)