from django.db import models
from .part import Part

class Mobo(Part):
    SOCKET_TYPES = (
        ('AM3+', 'AM3+'),
        ('AM4', 'AM4'),
        ('TR4', 'TR4'),
        ('LGA1151', 'LGA1151'),
        ('LGA2011-3', 'LGA2011-3'),
    )
    FORM_FACTORS = (
        ('ATX','ATX'),
        ('EATX','EATX'),
        ('XL ATX','XL ATX'),
        ('mATX','micro ATX'),
        ('mITX','mini ITX'),
    )
    CHIPSET_TYPES = (
        ('B450','AMD B450'),
        ('B350','AMD B350'),
        ('X470','AMD X470'),
        ('X370','AMD X370'),
        ('X399','AMD X399'),
        ('X570','AMD X570'),
        ('B360','Intel B360'),
        ('Z390','Intel Z390'),
        ('Z170','Intel Z170'),
        ('Z270','Intel Z270'),
        ('Z370','Intel Z370'),
    )
    socket = models.CharField(max_length=16, choices=SOCKET_TYPES) 
    chipset = models.CharField(max_length=16, choices=CHIPSET_TYPES)
    form_factor = models.CharField(max_length=8, choices=FORM_FACTORS)
    ram_slots = models.IntegerField()
    max_ram = models.IntegerField()
    sata = models.IntegerField()
    m2 = models.IntegerField()
    pcie = models.IntegerField()

    class Meta:
        ordering = ['chipset']

    def __str__(self):
        return "{} - {} {} {} Motherboard".format(self.manufacturer, self.chipset, self.form_factor, self.socket)

    @property
    def is_amd_board(self):
        return "AMD" in self.get_chipset_display()
            

