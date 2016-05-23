from django.db import models


class Option(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    first_vote = models.PositiveIntegerField(default=0)
    second_vote = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class HackNight(models.Model):
    date = models.DateField(auto_now=True)
    name = models.CharField(max_length=255)
    options = models.ManyToManyField(Option)

    def __str__(self):
        return self.name