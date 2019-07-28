from django.db import models
from .part import Part

class Memory(Part):
    speed = models.CharField(max_length=16)
    frequency = models.IntegerField()
    memory_type = models.CharField(max_length=16)
    isdual = models.BooleanField(default=False)
    ram = models.IntegerField(verbose_name='Memory')
    cas_latency = models.IntegerField()
    isecc = models.BooleanField(verbose_name='Is ECC')

    class Meta: 
        ordering = ['model_name']

    def __str__(self):
        memory_format = "{}x{}GB".format(2 if self.isdual else 1, self.ram//2 if self.isdual else self.ram )
        return "{} - {} {}".format(self.manufacturer, self.model_name, memory_format)

    @property
    def price_per_gb(self):
        """ memory price per gb """
        return self.price / self.ram