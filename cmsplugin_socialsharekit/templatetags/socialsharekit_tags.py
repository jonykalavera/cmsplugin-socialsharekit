# -*- coding: utf-8 -*-
import json
from pprint import pprint

from django import template
from django.utils.html import mark_safe

register = template.Library()


@register.filter
def toJSON(value):
    return mark_safe(json.dumps(value))

