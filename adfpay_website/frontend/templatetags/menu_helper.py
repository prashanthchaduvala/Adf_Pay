from django import template
from api.models import Product
from frontend.encryption_util import *

register = template.Library()


@register.simple_tag
def menu():
    menu = ''
    data = Product.objects.values('id','productname','upload','heading1','content1','content2','heading2','content3','heading3','content4','four_steps','step1heading','step1content','step2heading','step2content','step3heading','step3content','step4heading','step4content','eligibility_content','criteria1','criteria2','criteria3','criteria4','action')
    objs=[]
    for obj in data:
        print("something")

        obj['encrypt_key']=encrypt(obj['id'])
        obj['id']=obj['id']
        objs.append(obj)
        print(objs)
    for obj in objs:
        menu = menu +"<li><a href='/employees_details/"+str(obj['encrypt_key'])+"/'>"+obj['productname']+"</a></li>"
    return menu