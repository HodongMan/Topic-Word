from django.db import models

class Crime(models.Model):

    year = models.CharField(max_length=200, default="")
    area = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    occur = models.PositiveIntegerField(default=0)
    arrest = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("area", "location")
