from django import template
from crud_app.models import *
from authentication.models import ExtendUser

register = template.Library()


@register.filter(is_safe=True)
def myfilter(value):
    return value

register.filter('myfilter', myfilter)