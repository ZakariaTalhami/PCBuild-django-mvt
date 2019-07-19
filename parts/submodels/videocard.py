from django.db import models

class Videocard(models.Model):
    chipset = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    memory = models.IntegerField()
    base_clock = models.IntegerField()
    boost_clock = models.IntegerField()
    price = models.FloatField()

    