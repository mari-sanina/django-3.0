from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=350)
