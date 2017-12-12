from django.db import models
from django.utils import timezone


class Region(models.Model):
    name = models.CharField(max_length=200)
    population = models.CharField(max_length=200)
    field = models.CharField(max_length=200)
    center = models.CharField(max_length=200)
    governer = models.CharField(max_length=200)
    about = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    changed_date = models.DateTimeField(
            blank=True, null=True)

    def change(self):
        self.changed_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=200)
    center = models.CharField(max_length=200)
    about = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    created_date = models.DateTimeField(
            default=timezone.now)
    changed_date = models.DateTimeField(
            blank=True, null=True)

    def change(self):
        self.changed_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name