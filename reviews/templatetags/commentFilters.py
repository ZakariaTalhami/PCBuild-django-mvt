from django import template
from django.db import models

register = template.Library()

@register.filter(is_safe=True)
def iscommented(value, user_id):
    """
    Checks whether or not a user owns a comment from the queryset passed 
    """
    commented = True;
    try:
        value.get(owner=user_id)
    except models.ObjectDoesNotExist:
        commented = False
    return commented