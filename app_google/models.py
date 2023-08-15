from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    lat = models.FloatField(null=True, blank=True, default=47.1513451)
    lng = models.FloatField(null=True, blank=True, default=-126.1665193)
