from django import template
from api.models import Retailer

from frontend.encryption_util import *

register = template.Library()


@register.simple_tag
def menu():
    menu = ''
    
    data=Retailer.objects.values('id','retailername','upload','heading1','content1','content2','heading2','content3','heading3','content4','four_steps','step1heading','step1content','step2heading','step2content','step3heading','step3content','step4heading','step4content','eligibility_content','criteria1','criteria2','criteria3','criteria4','action')
    objs=[]
    for obj in data:
        print("something")

        obj['encrypt_key']=encrypt(obj['id'])
        obj['id']=obj['id']
        objs.append(obj)
        print(objs)
    for obj in objs:
        menu = menu +"<li><a href='/retailer_details/"+str(obj['encrypt_key'])+"/'>"+obj['retailername']+"</a></li>"
        # menu = menu +"<li><a href="{% url '/employee_detail/' id=brand.id %}"</a></li>"
        

    print(menu)
    return menu

    