from django import template

register = template.Library()

@register.filter(is_safe=True)
def dictvalue(value: dict, key):
    """
    Retrieve a value from a passed dictionary, using a key value
    """
    return value.get(key)