from django.db import models
from .part import Part

class Storage(Part): 
    INTERFACE_TYPES = (
        ('SATA', "Serial ATA"),
        ('FC', "Fiber Channel"),
        ('SAS', "Serial attached SCSI"),
        ('PCIe', "Peripheral Component Interconnect Express"),
        ('USB', "USB"),
    )
    capacity = models.IntegerField()
    cache = models.IntegerField()
    interface = models.CharField(max_length=16, choices=INTERFACE_TYPES) # enum

    def __str__(self):
        if self.capacity > 1023:
            return "{} {} TB".format(self.model_name, self.capacity/1024)
        else:
            return "{} {} GB".format(self.model_name, self.capacity)
        
        
    @property
    def price_per_gb(self):
        """ Storage price per gb """
        return self.price / self.capacity