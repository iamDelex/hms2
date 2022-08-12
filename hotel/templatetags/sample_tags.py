from django import template
from django.urls import reverse


register = template.Library()

@register.simple_tag
def intralink(link, section):
    return reverse(link) + '#' + section
