from django import template

register = template.Library()


@register.filter('my_filter')
def my_filter(value, arg):
    return value.split(arg)


@register.simple_tag
def my_tag(a, b, c=None):
    return f"{a} {b} {c}"


# register.filter('my_filter', my_filter)
