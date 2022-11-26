from django import template
from cvapp.models import *

register = template.Library()

@register.simple_tag()
def get_pdf(cv_id=0):
    print(cv_id)