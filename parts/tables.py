import django_tables2 as tables
from django_tables2.utils import A
from .models import Cpu, Mobo, Memory, Storage, Videocard

class PartMeta:
    """ 
        A base meta class for Part Table classes, 
        defining CSS classes and templates for tables 
    """
    attrs = {'class': 'table part-grid table-hover'}
    template_name='django_tables2/bootstrap-responsive.html'
    exclude = ('part_ptr',)

class CpuTable(tables.Table):
    id = tables.LinkColumn('parts-cpu-detail', args=[A('pk')])

    class Meta(PartMeta):
        model = Cpu
    
class MoboTable(tables.Table):
    id = tables.LinkColumn('parts-mobo-detail', args=[A('pk')])

    class Meta(PartMeta):
        model = Mobo

class MemoryTable(tables.Table):
    id = tables.LinkColumn('parts-memory-detail', args=[A('pk')])

    class Meta(PartMeta):
        model = Memory

class StorageTable(tables.Table):
    id = tables.LinkColumn('parts-storage-detail', args=[A('pk')])

    class Meta(PartMeta):
        model = Storage

class VideocardTable(tables.Table):
    id = tables.LinkColumn('parts-videocard-detail', args=[A('pk')])

    class Meta(PartMeta):
        model = Videocard