from django import templates

register = template.libray()

@register.filter(name='cut')
def cut(value,arg):
    """
    it will cut the arg from the values
    """
    return replace(arg,"")

