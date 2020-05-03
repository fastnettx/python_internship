from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def slice(value, count):
    return value[:count] + "-"


@register.filter
@stringfilter
def after_slice(value, count):
    return value[count:]
