from django.db import models

class Videocard(models.Model):
    manufacturer = models.CharField(max_length=64)
    chipset = models.CharField(max_length=64)
    model_name = models.CharField(max_length=64)
    part_number = models.CharField(max_length=18)
    memory = models.IntegerField()
    base_clock = models.IntegerField()
    boost_clock = models.IntegerField()
    price = models.FloatField()

    class meta:
        ordering = ['model_name']

    def __str__(self):
        return "{} - {} {}GB {}".format(self.manufacturer, self.chipset, self.memory, self.model_name)