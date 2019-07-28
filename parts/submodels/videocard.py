from django.db import models
from .part import Part

class Videocard(Part):
    chipset = models.CharField(max_length=64)
    vram = models.IntegerField(verbose_name='Memory')
    base_clock = models.IntegerField()
    boost_clock = models.IntegerField()

    class Meta:
        ordering = ['model_name']

    def __str__(self):
        return "{} - {} {}GB {}".format(self.manufacturer, self.chipset, self.vram, self.model_name)