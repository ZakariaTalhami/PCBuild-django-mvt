import django_tables2 as tables
from django_tables2.utils import A
from .models import Cpu

class CpuTable(tables.Table):
    id = tables.LinkColumn('parts-cpu-detail', args=[A('pk')])
    class Meta:
        model = Cpu
        attrs = {'class': 'table'}
        template_name='django_tables2/bootstrap-responsive.html'