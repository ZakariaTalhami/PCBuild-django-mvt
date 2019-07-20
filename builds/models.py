from django.db import models
from parts.models import Cpu, Memory, Mobo, Storage, Videocard

# Create your models here.
class PcBuild(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    cpu = models.ForeignKey(Cpu, null=True, blank=True, on_delete=models.SET_NULL)
    mobo = models.ForeignKey(Mobo, null=True, blank=True, on_delete=models.SET_NULL)
    storage = models.ManyToManyField(Storage)
    videocard = models.ManyToManyField(Videocard)
    memory = models.ManyToManyField(Memory)
    # TODO: implement the users model
    # likes = models.ManyToManyField(Users)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    # TODO: calculate the price from the parts
    def calculate_price(self):
        return -1
    
    # TODO: check the compatability from the parts
    def check_compatability(self):
        pass
