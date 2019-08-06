from django.template import Template
from django.test import TestCase  
import html

class TemplateTestCase(TestCase):

    def template_assert(self, filter_module, template, context, expected, unescape=True):
            t = Template('{%% load %s %%}%s' % (filter_module, template))
            if unescape :
                self.assertEqual(html.unescape(t.render(context)), expected)
            else:
                self.assertEqual(t.render(context), expected)
