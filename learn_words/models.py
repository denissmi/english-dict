from __future__ import unicode_literals

from django.db import models


class EnglishWord(models.Model):
    word = models.CharField(max_length=64)
    translation = models.CharField(max_length=256)
    rate = models.IntegerField(default=0)

    class Meta:
        ordering = ('word',)


class RussianWord(models.Model):
    word = models.CharField(max_length=64)
    translation = models.CharField(max_length=256)
    rate = models.IntegerField(default=0)

    class Meta:
        ordering = ('word',)
