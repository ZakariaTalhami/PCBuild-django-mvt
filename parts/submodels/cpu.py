from django.db import models

class Cpu(models.Model):
    manufacturer = models.CharField(max_length=16)
    series = models.CharField(max_length=16)
    model_name = models.CharField(max_length=16)
    part_number = models.CharField(max_length=18)
    family = models.CharField(max_length=16)
    cores = models.IntegerField()
    threads = models.IntegerField()
    base_clock = models.FloatField()
    boost_clock = models.FloatField()
    # price = models.FloatField()

    class Meta:
        ordering = ['series']

    def __str__(self):
        return "{} - {} {} {}GHz {}-Cores Processor".format(self.manufacturer, self.series, self.model_name, self.base_clock, self.cores)