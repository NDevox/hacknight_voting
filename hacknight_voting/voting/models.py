from django.db import models


class Option(models.model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    first_vote = models.PositiveIntegerField()
    second_vote = models.PositiveIntegerField()


class HackNight(models.model):
    name = models.CharField(max_length=255)
    options = models.ManyToManyField(Option)