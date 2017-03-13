from __future__ import unicode_literals

from django.db import models


class EnglishWord(models.Model):
    word = models.CharField(max_length=64)
    translation = models.CharField(max_length=256)
    rate = models.IntegerField(default=0)

    owner = models.ForeignKey('auth.User', related_name='english_words', on_delete=models.CASCADE)

    class Meta:
        ordering = ('word',)


class RussianWord(models.Model):
    word = models.CharField(max_length=64)
    translation = models.CharField(max_length=256)
    rate = models.IntegerField(default=0)

    owner = models.ForeignKey('auth.User', related_name='russian_words', on_delete=models.CASCADE)

    class Meta:
        ordering = ('word',)
