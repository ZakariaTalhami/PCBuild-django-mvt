from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from .models import Cpu, Memory, Mobo, Storage, Videocard
from .forms import CpuForm
from .tables import CpuTable, MemoryTable, MoboTable, StorageTable, VideocardTable
from django.views.generic.detail import DetailView
from django_tables2.views import SingleTableView

## Parent View Classes
class PartDetailView(DetailView):
    """
        Renders the view for part details, it overwites the funtion 'get_context_data'
        to add to the context the string representation of the objecta as a title and
        the object itself as a dictionary.
    """
    def get_context_data(self, **kwargs):
        context  = {}
        if self.object:
            context['title'] = str(self.object)
            fields = self.model._meta.get_fields()
            context['part'] = {field.verbose_name:getattr(self.object, field.name) for field in fields if field.concrete and not field.one_to_one}
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = context['part']
            context['comments'] = self.object.comment_set.all()
        context.update(kwargs)
        return context
            
class PartListView(SingleTableView):

    """ 
        create as view that generates the filter option of a model and addes them
        to the context
    """

    context_filters_name = 'filters'
    
    def get_table_filters(self, **kwargs):
        """ Generate the filter option from the model fields and object list """
        fields = self.model._meta.get_fields()
        values = self.object_list.values()
        filter_values = {}
        for field in fields:
            if field.name != 'id' and field.concrete and not field.one_to_one:
                filter_values[field.verbose_name] = set([ part[field.name] for part in values])
        return filter_values

    def get_context_filters_name(self):
        """Get the name of the item to be used in the context."""
        return self.context_filters_name

    def get_context_data(self, **kwargs):
        """Add the filter option to the context"""
        context = {}
        context[self.get_context_filters_name()] = self.get_table_filters()
        context.update(kwargs)
        return super().get_context_data(**context)


# Child View Classes
class CpuDetailView(PartDetailView):
    model = Cpu
    template_name = 'parts/cpu/details.html'
    context_object_name = 'cpu_part'

class CpuListView(PartListView):
    model = Cpu
    table_class = CpuTable
    template_name = 'parts/cpu/index.html'

class CpuCreate(CreateView):
    model = Cpu
    template_name = "cpus/create.html"
    form_class = CpuForm


class MoboDetailView(PartDetailView):
    model = Mobo
    template_name = 'parts/cpu/details.html'
    context_object_name = 'cpu_part'

class MoboListView(PartListView):
    model = Mobo
    table_class = MoboTable
    template_name = 'parts/cpu/index.html'


class StorageDetailView(PartDetailView):
    model = Storage
    template_name = 'parts/cpu/details.html'
    context_object_name = 'cpu_part'

class StorageListView(PartListView):
    model = Storage
    table_class = StorageTable
    template_name = 'parts/cpu/index.html'


class MemoryDetailView(PartDetailView):
    model = Memory
    template_name = 'parts/cpu/details.html'
    context_object_name = 'cpu_part'

class MemoryListView(PartListView):
    model = Memory
    table_class = MemoryTable
    template_name = 'parts/cpu/index.html'


class VideocardDetailView(PartDetailView):
    model = Videocard
    template_name = 'parts/cpu/details.html'
    context_object_name = 'cpu_part'

class VideocardListView(PartListView):
    model = Videocard
    table_class = VideocardTable
    template_name = 'parts/cpu/index.html'