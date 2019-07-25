from .models import Cpu
from django.forms import ModelForm

class CpuForm(ModelForm):
    class Meta:
        model = Cpu
        exclude = ['id']