from django.shortcuts import render, reverse
from django.views.generic.edit import CreateView
# models
from .models import Cpu, Memory, Mobo, Storage, Videocard
from django.http import HttpResponseRedirect
from .forms import CpuForm
from .tables import CpuTable

# 
from django.views.generic.detail import DetailView

class PartDetailView(DetailView):


    def get_object(self, queryset=None):
        part_object = super().get_object(queryset=queryset)
        fields = self.model._meta.get_fields()
        return {field.verbose_name:getattr(part_object, field.name) for field in fields if field.concrete}


# 



def cpuList(request):
    cpu_list = Cpu.objects.all()
    table = CpuTable(cpu_list)
    context = {
        'cpu_list': cpu_list,
        'table': table
    }
    return render(request, 'parts/cpu/index.html', context=context)
    
    # TODO: make my own mixin for this as it would be repeated many times, or custom view class
def cpuDetail(request, pk):
    # TODO: Find a way to set display names and get them in the list and get __str__
    cpu_item = Cpu.objects.values().get(pk=pk)
    context = {
        'cpu_part': cpu_item
    }
    return render(request, "parts/cpu/details.html", context=context)

class  CpuCreate(CreateView):
    model = Cpu
    template_name = "cpus/create.html"
    form_class = CpuForm