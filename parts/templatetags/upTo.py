from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def upto(value: str, delimiter=','):
    """
    Split a string and return the first token of the string before the specific 
    delimiter. e.g 'Yes miss daisy, ill be honking' returns 'Yes miss daisy'
    """
    return value.split(delimiter)[0]