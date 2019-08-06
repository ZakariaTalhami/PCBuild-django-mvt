from django import template

register = template.Library()

@register.filter(is_safe=False)
def get_global_error(value: dict):
    """
    Takes a dictionary of errors and returns the value of the key '__all__',
    which represents the  global errors of a form and not an error of a specific 
    field
    """
    return value.get('__all__', False);
