from django import template

register = template.Library()

# see http://stackoverflow.com/a/2308693/1425689
def field_type(field, ftype):
    try:
        t = field.field.widget.__class__.__name__
        return t.lower() == ftype
    except:
        pass
    return False

register.filter('field_type', field_type)
