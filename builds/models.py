from django.db import models
from parts.models import Cpu, Memory, Mobo, Storage, Videocard
from django.contrib.auth import get_user_model
    

# Create your models here.
class PcBuild(models.Model):
    owner = models.ForeignKey(get_user_model(), null=True, blank=False, on_delete=models.CASCADE, related_name="owner",)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    cpu = models.ForeignKey(Cpu, null=True, blank=True, on_delete=models.SET_NULL)
    mobo = models.ForeignKey(Mobo, null=True, blank=True, on_delete=models.SET_NULL)
    storage = models.ManyToManyField(Storage, blank=True)
    videocard = models.ManyToManyField(Videocard, blank=True)
    memory = models.ManyToManyField(Memory, blank=True)
    likes = models.ManyToManyField(get_user_model(), blank=True, related_name="likes")

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
