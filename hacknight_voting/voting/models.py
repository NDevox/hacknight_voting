from django.db import models


class Option(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    first_vote = models.PositiveIntegerField()
    second_vote = models.PositiveIntegerField()


class HackNight(models.Model):
    date = models.DateField(auto_now=True)
    name = models.CharField(max_length=255)
    options = models.ManyToManyField(Option)