from django import template

register = template.Library()

EN_TO_FA = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")

@register.filter(name='translate_number')
def translate_number(value):
    try:
        return str(value).translate(EN_TO_FA)
    except:
        return value
        