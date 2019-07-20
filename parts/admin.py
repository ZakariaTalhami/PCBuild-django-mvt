from django.contrib import admin
from .models import Cpu
from .models import Memory
from .models import Mobo
from .models import Storage
from .models import Videocard

models = [
    Cpu, 
    Memory, 
    Mobo, 
    Storage, 
    Videocard
]
# Register your models here.
admin.site.register(models)

