from django import template
from django.utils.translation import gettext

register = template.Library()

@register.filter
def trans(value):
    return gettext(value)
