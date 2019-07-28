from django.db import models
from django.shortcuts import reverse
from .part import Part

class Cpu(Part):
    series = models.CharField(max_length=16)
    family = models.CharField(max_length=16)
    cores = models.IntegerField()
    threads = models.IntegerField()
    base_clock = models.FloatField()
    boost_clock = models.FloatField()

    class Meta:
        ordering = ['series']

    def __str__(self):
        return "{} - {} {} {}GHz {}-Cores Processor".format(self.manufacturer, self.series, self.model_name, self.base_clock, self.cores)

    def get_absolute_url(self):
        return reverse('parts-cpu-list')