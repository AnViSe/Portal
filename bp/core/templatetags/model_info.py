from django import template
from django.urls import reverse_lazy

register = template.Library()


@register.filter(name='title')
def verbose_name(obj):
    return obj._meta.verbose_name


@register.filter
def verbose_name_plural(obj):
    return obj._meta.verbose_name_plural


@register.filter
def get_list_url(obj):
    if obj.Params.route_list:
        return reverse_lazy(obj.Params.route_list)
    else:
        return '#'


@register.filter(name='fields')
def verbose_name(obj):
    return obj._meta.fields


@register.filter
def field_label(field):
    return field.verbose_name


@register.filter
def field_value(obj, field):
    return getattr(obj, field)
