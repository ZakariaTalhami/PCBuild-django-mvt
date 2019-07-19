from django.db import models

class Storage(models.Model): 
    INTERFACE_TYPES = (
        ('SATA', "Serial ATA"),
        ('FC', "Fiber Channel"),
        ('SAS', "Serial attached SCSI"),
        ('PCIe', "Peripheral Component Interconnect Express"),
        ('USB', "USB"),
    )
    name = models.CharField(max_length=64)
    capacity = models.IntegerField()
    cache = models.IntegerField()
    interface = models.CharField(max_length=16, choices=INTERFACE_TYPES) # enum
    price = models.FloatField()

    def __str__(self):
        if self.capacity > 1023:
            return "{} {} TB".format(self.name, self.capacity)
        else:
            return "{} {} GB".format(self.name, self.capacity/1024)
        

    @property
    def price_per_gb(self):
        """ Storage price per gb """
        return self.price / self.capacity