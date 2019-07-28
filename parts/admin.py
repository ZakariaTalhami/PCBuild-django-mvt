from django.contrib import admin
from .models import Part, Cpu, Memory, Mobo, Storage, Videocard

models = [
    Part,
    Cpu, 
    Memory, 
    Mobo, 
    Storage, 
    Videocard
]
# Register your models here.
admin.site.register(models)

