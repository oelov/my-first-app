from django.conf import settings
from django.db import models
from django.utils import timezone


class Player(models.Model):
    slug = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=25)
    club = models.CharField(max_length=50)

    def __str__(self):
        return self.name
