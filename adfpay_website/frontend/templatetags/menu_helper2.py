from django import template
from api.models import Professional
from frontend.encryption_util import *
register = template.Library()


@register.simple_tag
def menu():
    menu = ''
    data=Professional.objects.values('id','professionalname','upload','heading1','content1','content2','heading2','content3','heading3','content4','four_steps','step1heading','step1content','step2heading','step2content','step3heading','step3content','step4heading','step4content','eligibility_content','criteria1','criteria2','criteria3','criteria4','action')
    objs=[]
    for obj in data:
        print("something")

        obj['encrypt_key']=encrypt(obj['id'])
        obj['id']=obj['id']
        objs.append(obj)
        print(objs)
    for obj in objs:
        menu = menu +"<li><a href='/profession_detail/"+str(obj['encrypt_key'])+"/'>"+obj['professionalname']+"</a></li>"
        # menu = menu +"<li><a href="{% url '/employee_detail/' id=brand.id %}"</a></li>"
        

    print(menu)
    return menu
