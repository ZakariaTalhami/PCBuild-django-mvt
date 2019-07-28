from django.db import models

class Part(models.Model):
    manufacturer = models.CharField(max_length=16)
    model_name = models.CharField(max_length=16)
    part_number = models.CharField(max_length=18)
    price = models.FloatField()