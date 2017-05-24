from django.db import models


class Driver(models.Model):
    number = models.CharField(max_length=11)
    last_latitude = models.FloatField(null=True)
    last_longitude = models.FloatField(null=True)
