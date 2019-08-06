from django.test import TestCase
from django.shortcuts import reverse
from django.template import Context, Template 
from common.testing.object_factory import json_to_objects 
from common.testing.custom_testcases import TemplateTestCase 
from unittest.mock import patch
from .models import Memory, Cpu
import json
import os
import html

LIST_NO_DATA_FILTERS = "No Filters for {}"
LIST_NO_DATA_TABLE = "There arent any {}"
OBJECT_JSON_PATH = 'submodels/test_objects/memory_objects.json'
DETAIL_VIEW_NAMESPACE = 'parts-memory-detail'
LIST_VIEW_NAMESPACE = 'parts-memory-list'

class MemoryModelTest(TestCase):

    def setUp(self):
        dir = os.path.dirname(__file__)
        json_to_objects(os.path.join(dir, OBJECT_JSON_PATH))

    def test_price_per_gb(self):
        mem = Memory.objects.all();
        
        for memory in mem:
            self.assertEqual(memory.price_per_gb, memory.price / memory.ram)

    def test_memory_str(self):
        memory = Memory.objects.get(pk=1)
        expected = "Corsair - Vengeance 2x8GB" 
        self.assertEqual(str(memory), expected)
        
        
class CpuModelTest(TestCase):

    def test_cpu_str(self):
        expected = "AMD - Ryzen 5 3600 3.8GHz 6-Cores Processor"
        cpu = Cpu(
            manufacturer= "AMD",
            series= "Ryzen 5",
            model_name= "3600",
            base_clock= 3.8,
            cores= 6,
        )
        self.assertEqual(str(cpu), expected)


class PartDetailViewTest(TestCase):

    def setUp(self):
        dir = os.path.dirname(__file__)
        json_to_objects(os.path.join(dir, OBJECT_JSON_PATH))

    def test_get_context_data(self):
        response = self.client.get(reverse(DETAIL_VIEW_NAMESPACE, kwargs={ 'pk':1}))
        mem = Memory.objects.get(pk=1)
        res_context = response.context_data;

        self.assertIn('title', res_context)
        self.assertEqual(response.context_data['title'], str(mem))
        self.assertIn('part', res_context)
        self.assertIn('cpu_part', res_context)
        self.assertEqual(res_context['object'], mem)


class PartListViewTest(TestCase):

    def create_data(self):
        dir = os.path.dirname(__file__)
        json_to_objects(os.path.join(dir, OBJECT_JSON_PATH))

    def test_get_context_filters_name(self):
        self.create_data()
        response = self.client.get(reverse(LIST_VIEW_NAMESPACE))
        fields = Memory._meta.get_fields()
        verbose_names = [field.verbose_name for field in fields if field.concrete]

        # Assert filter generation
        self.assertIn('filters', response.context_data)
        res_filters = response.context_data['filters']
        for key,value in res_filters.items():
            self.assertIn(key, verbose_names)
            self.assertEqual(len(value), len(set(value)))
        
        # Assert HTML
        self.assertContains(response, 'Filters')
        self.assertContains(response, 'Parts')
        self.assertContains(response, 'PC Buildathon')

    def test_no_parts_found(self):
        response = self.client.get(reverse(LIST_VIEW_NAMESPACE))

        model_verbose_name = response.context_data['table'].data.verbose_name_plural
        self.assertContains(response, LIST_NO_DATA_FILTERS.format(model_verbose_name))
        self.assertContains(response, LIST_NO_DATA_TABLE.format(model_verbose_name))
        
class CustomFiltersTest(TemplateTestCase):

    def test_dictvalue(self):
        expected = {
            "what" : 'first line of data',
            "second" : ['list','of','strings'],
            'third': { 'dict': 'placeholder' }
        }
        
        template_template = '{{ dicti|dictvalue:"%s" }}'
        context = Context({'dicti': expected})
        for key,value in expected.items() :
            self.template_assert(
                filter_module = 'dictvalue',
                template = template_template % key,
                context = context,
                expected = str(value),
            )

    def test_form_filters(self):
        expected = {
            "__all__" : 'All error',
        }
        expected_false = {}
        template_template = "{{ %s|get_global_error }}"
        context = Context({"value":expected, 'noValue':expected_false})
        self.template_assert(
            filter_module = 'formfilters',
            template = template_template % 'value',
            context = context,
            expected = str(expected['__all__']),
        )

        self.template_assert(
            filter_module = 'formfilters',
            template = template_template % 'noValue',
            context = context,
            expected = str(False),
        )

    def test_upto_filter(self):
        text = "sometext, that continues. Then stops."
        template_template = "{{ text|upto }}"
        template_template2 = "{{ text|upto:'%s' }}"
        context = Context({'text':text})
        self.template_assert(
            filter_module = 'upTo',
            template = template_template,
            context = context,
            expected = 'sometext',
        )
        self.template_assert(
            filter_module = 'upTo',
            template = template_template2 % ',',
            context = context,
            expected = 'sometext',
        )
        self.template_assert(
            filter_module = 'upTo',
            template = template_template2 % '.',
            context = context,
            expected = 'sometext, that continues',
        )
        self.template_assert(
            filter_module = 'upTo',
            template = template_template2 % '?',
            context = context,
            expected = text,
        )



        