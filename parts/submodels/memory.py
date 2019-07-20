from django.db import models

class Memory(models.Model):
    manufacturer = models.CharField(max_length=16)
    model_name = models.CharField(max_length=64)
    part_number = models.CharField(max_length=18)
    speed = models.CharField(max_length=16)
    frequency = models.IntegerField()
    memory_type = models.CharField(max_length=16)
    isdual = models.BooleanField(default=False)
    memory = models.IntegerField()
    cas_latency = models.IntegerField()
    isecc = models.BooleanField()
    price = models.FloatField()

    class Meta: 
        ordering = ['model_name']

    def __str__(self):
        memory_format = "{}x{}GB".format(2 if self.isdual else 1, self.memory//2 if self.isdual else self.memory )
        return "{} - {} {}".format(self.manufacturer, self.model_name, memory_format)

    @property
    def price_per_gb(self):
        """ memory price per gb """
        return self.price / self.memory