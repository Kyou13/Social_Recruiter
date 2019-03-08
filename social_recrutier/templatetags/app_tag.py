from django import template
register = template.Library()

@register.filter
def index(value, args):
  return (int(value)-1) * 10 + int(args)
