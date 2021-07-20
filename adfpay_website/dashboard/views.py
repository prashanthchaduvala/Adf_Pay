from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import *
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
import string
from datetime import datetime, timedelta
import math
from django.urls import reverse
import re
from django.core.mail import send_mail
from django.conf import settings
import smtplib
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.core.files.storage import FileSystemStorage 
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from dashboard.models import *
from frontend.encryption_util import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from accounts.models import *
import requests


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admindashboard(request):
    return render(request,'dashboard/admin_dashboard.html')


def check_user_functions(request, objectType):
    if request.user.is_superuser:
        return True
    internal_user = InternalUsers.objects.get(user_id=request.user.id)
    function_names = eval(internal_user.function_names)
    if objectType not in function_names and 'all' not in function_names:
        return False
    return True


def create_perission_name(request):
    if request.method == "POST":
        permission_menu = request.POST.get("permission_menu")
        status = request.POST.get("status")
        messages.success(request, 'Account Created Successfully! Check your email for the password details.')
        return redirect('show_object_list', objectType='PermissionMenu')
    return render(request, "dashboard/RegisterForm.html", context = {'operation':'create'})


def edit_perission_name(request,id):
    if request.method == "POST":
        menu=PermissionMenu.objects.get(id=id)
        permission_menu = request.POST.get("permission_menu")
        status = request.POST.get("status")
        menu.permission_menu=permission_menu
        menu.status=status
        menu.save()
        messages.success(request, 'Edited Successfully.')
        return redirect('menu_permission_list')
    return render(request, "dashboard/RegisterForm.html", context = {'operation':'create'})


def model_object(request, objectType):
    ckeditor_list = ['PublishBlogs', 'ManageNewsMedia','TermsAndConditions', 'TermsOfUse', 'FairPracticeCode', 'PrivacyPolicy', 'Disclaimer', 'GrievanceAddressMechanism', 'Faq', 'LifeAtAdfpay']
    if not check_user_functions(request, objectType):
        messages.error(request, 'You are not allowed to add entry to this {} model!'.format(objectType))
        return redirect('dashboard')
    if 'edit' in request.GET:
        if not check_permission_types(request, 'update'):
            messages.error(request, 'You do not have update access!')
            return redirect('dashboard')
        objectId = request.GET['objectId']
        objToUpdate = getDBObject(objectType,'modelObjects',objectId)
        context = {
            "objectType": objectType,
            "objectToUpdate":objToUpdate,
        }
        if objectType in ckeditor_list:
            objectTypeForm = objectType + 'Form'
            form = getFormClass(request, objectTypeForm, 'editform', objToUpdate)
            context['form'] = form
        templateFile = 'neoadmin/adminforms/'+objectType+'Form.html'
        return render(request,templateFile, context)
    else:
        if not check_permission_types(request, 'create'):
            messages.error(request, 'You do not have create access!')
            return redirect('dashboard')
        context = {
            "objectType": objectType,
        }
        if objectType in ckeditor_list:
            objectTypeForm = objectType + 'Form'
            form = getFormClass(request, objectTypeForm, 'modelform')
            context['form'] = form
        templateFile = 'dashboard/adminforms/'+objectType+'Form.html'
        return render(request,templateFile, context)




def menu_permission_list(request,objectType='PermissionMenu'):
    context={}
    if request.method == "POST":
        obj=PermissionMenu(permission_menu=request.POST['permission_menu'],status=request.POST['status'])
        obj.save()
        return redirect('menu_permission_list')
    context['menu']=PermissionMenu.objects.filter(status=1)


    print(context['menu'])
    return render(request, 'dashboard/RegisterForm.html', context)


def sub_menu_permission_list(request,objectType='PermissionMenu'):
    context={}
    if request.method == "POST":
        menu=PermissionMenu.objects.get(id=request.POST['menu_id'])
        obj=PermissionSubMenu(permission_sub_menu=request.POST['permission_sub_menu'],status=request.POST['status'],menu_id=menu)
        obj.save()
        return redirect('sub_menu_permission_list')

    context['submenu']=PermissionSubMenu.objects.filter(status=1)
    context['menu']=PermissionMenu.objects.filter(status=1)
    print(context['submenu'])
    return render(request, 'dashboard/permission_sub_menu.html', context)




def putSpace(input):
    words = re.findall('[A-Z][a-z]*', input)
    result = []
    for word in words:
        word = chr( ord (word[0]) + 32) + word[1:]
        result.append(word)
    return ' '.join(result).title()


@csrf_exempt
def change_action(request, objectType, objectId):
     modelClass = globals()[objectType]
     model = modelClass.objects.get(id=objectId)
     action = request.GET['action']
     model.action = action
     model.save()
     return HttpResponse('Action Changed!')


def getDBObject(objectType,caller,objectId=None):
    modelClass = globals()[objectType]
    if caller == 'modelObjects':
        return modelClass.objects.filter(id=objectId).values()[0]
    elif caller == 'dynamicModelObjects':
        return modelClass.objects.filter(id=objectId).values()[0]
    elif caller == 'updateObject':
        return modelClass.objects.get(id=objectId)
    elif caller == 'showObjectDetails':
        return modelClass.objects.filter(id=objectId).values()[0]
    elif caller == 'showObjectList':
        return modelClass.objects.all().values()
    elif caller == 'saveObject':
        return modelClass()

def getFormClass(request, objectTypeForm, caller, objToUpdate=None):
    formClass = globals()[objectTypeForm]
    if caller == 'modelform':
        return formClass()
    elif caller == 'editform':
        return formClass(initial=objToUpdate)
    elif caller == 'saveform':
        return formClass(request.POST)

def return_object_list(objList):
    objectList = list()
    for singleObject in objList:
        obj = dict()
        for key in singleObject:
            new_key = key.replace('_', ' ').title() if key != 'id' else 'Process Names' if key == 'function_names' else 'id'
            if key == 'action':
                if singleObject[key] == 'Active':
                    obj[new_key] = 'checked'
                else:
                    obj[new_key] = ''
            else:
                obj[new_key] = singleObject[key]
        objectList.append(obj)
    if len(objectList) > 0:
        if len(objectList[0]) > 2:
            fieldNames = [x for x in objectList[0]]
        noEntry = False
    else:
        fieldNames = []
        noEntry = True

    return noEntry, fieldNames, objectList

def check_user_functions(request, objectType):
    if request.user.is_superuser:
        return True
    internal_user = InternalUsers.objects.get(user_id=request.user.id)
    function_names = eval(internal_user.function_names)
    if objectType not in function_names and 'all' not in function_names:
        return False
    return True


def check_permission_types(request, permission):
    if request.user.is_superuser:
        return True
    internal_user = InternalUsers.objects.get(user_id=request.user.id)
    permission_types = eval(internal_user.permission_types)
    if permission not in permission_types:
        return False
    return True

@csrf_exempt
def deleteObject(request,objectType,objectId):
    if not check_user_functions(request, objectType):
        messages.error(request, 'You are not allowed to delete entry of this {} model!'.format(objectType))
        return redirect('dashboard')
    elif not check_permission_types(request, 'delete'):
        messages.error(request, 'You do not have delete access!')
        return redirect('dashboard')
    objToUpdate = getDBObject(objectType,'updateObject',objectId)
    objToUpdate.delete()
    messages.error(request, 'Record Deleted!')
    return redirect('internal_user_list')


    
@login_required
def subscription_payment(request):
    # obj = subscription_payment.objects.all()
    ##api has to be fetch########
    return render(request,'dashboard/subscription_payment.html',)


def new_review(request):
    res = requests.get('http://127.0.0.1:8000/api/v1/reviews/')
    json_data = res.json()
    for item in json_data:
        print(item, 'pppppppppppppasssssworddddd')
    return render(request,'dashboard/new_review.html',{'json_data': item})


def allocated_review(request):
    ##api has to be fetch########
    ##api has to be fetch########
    return render(request,'dashboard/allocated_review.html',)

def review_reply_received(request):
    ##api has to be fetch########
    ##api has to be fetch########
    return render(request,'dashboard/review_reply_received.html',)

def review_reply_responded(request):
    ##api has to be fetch########
    ##api has to be fetch########
    return render(request,'dashboard/review_reply_responded.html',) 

def review_pending(request):
    ##api has to be fetch########
    ##api has to be fetch########
    return render(request,'dashboard/review_pending.html',) 

def review_all(request):
    ##api has to be fetch########
    ##api has to be fetch########
    return render(request,'dashboard/review_all.html',)  

def new_feedback(request):
    res = requests.get('http://127.0.0.1:8000/api/v1/feedback/')
    json_data = res.json()
    for item in json_data:
        print(item, 'pppppppppppppasssssworddddd')
    return render(request,'dashboard/new_feedback.html', {'json_data': item})


def allocated_feedback(request):
    ##api has to be fetch########
    ##api has to be fetch########
    return render(request,'dashboard/allocated_feedback.html',)

def feedback_reply_received(request):
    ##api has to be fetch########
    ##api has to be fetch########
    return render(request,'dashboard/feedback_reply_received.html',)

def feedback_reply_responded(request):
    ##api has to be fetch########
    ##api has to be fetch########
    return render(request,'dashboard/feedback_reply_responded.html',)

def feedback_pending(request):
    ##api has to be fetch########
    ##api has to be fetch########
    return render(request,'dashboard/feedback_pending.html',)  

def all_feedback(request):
    ##api has to be fetch########
    ##api has to be fetch########
    return render(request,'dashboard/all_feedback.html',)    

def new_inovative_idea(request):
    ##api has to be fetch########
    ##api has to be fetch########
    return render(request,'dashboard/new_inovative_idea.html',)  


def inovative_idea_allocated(request):
    ##api has to be fetch########
    ##api has to be fetch########
    return render(request,'dashboard/inovative_idea_allocated.html',)

def inovative_idea_reply_received(request):
    ##api has to be fetch########
    ##api has to be fetch########
    return render(request,'dashboard/inovative_idea_reply_received.html',)  


def inovative_idea_reply_responded(request):
    ##api has to be fetch########
    ##api has to be fetch########
    return render(request,'dashboard/inovative_idea_reply_responded.html',)
def inovative_idea_implemented(request):
    ##api has to be fetch########
    ##api has to be fetch########
    return render(request,'dashboard/inovative_idea_implemented.html',)  


def inovative_idea_pending(request):
    ##api has to be fetch########
    ##api has to be fetch########
    return render(request,'dashboard/inovative_idea_pending.html',)

def inovative_idea_all(request):
    ##api has to be fetch########
    ##api has to be fetch########
    return render(request,'dashboard/inovative_idea_all.html',) 

def subscription_payment(request):
    # obj = subscription_payment.objects.all()
    res = requests.get('http://127.0.0.1:8000/api/v1/subscribers/')
    json_data = res.json()
    for item in json_data:
        print(item, 'pppppppppppppasssssworddddd')
    return render(request,'dashboard/subscription_payment.html',{'json_data': item})
            
def android(request):
    obj_data = Android.objects.values('ad_id','version','release_date','images','action')
    objs=[]
    for obj in obj_data:

        obj['encrypt_key']=encrypt(obj['ad_id'])
        obj['ad_id']=obj['ad_id']
        objs.append(obj)
    return render(request,'dashboard/android.html',{'obj':objs})



# Add Publish blog.
def add_android(request):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        file1 = file.get('images')
        # now = datetime.datetime.now().time()
        # merge_file = str(file1)+str(now)
        release_date = form.get('release_date')
        version = form.get('version')
        Android.objects.create(version=version,release_date=release_date,images=file1)
        return redirect('/dashboard/android/')
    else:
        return render(request,'dashboard/add_android.html')


# Edit Publish blog.
def edit_android(request,id):
    id=decrypt(id)
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        file1 = file.get('images')
        now = datetime.datetime.now().time()
        release_date = form.get('release_date')
        version = form.get('version')
        content_d_type = form.get('content_d_type')
        nm_editor = form.get('nm_editor')
        if file1:
            myfile = request.FILES['images']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            Android.objects.create(images=file1)
            Android.objects.filter(ad_id=id).update(version=version,release_date=release_date,images=filename)  
        obj = Android.objects.filter(ad_id=id)

        Android.objects.filter(ad_id=id).update(version=version,release_date=release_date)
        return redirect('/dashboard/android/')
    else:
        obj = Android.objects.filter(ad_id=id)

        return render(request,'dashboard/edit_android.html',{'obj':obj})


# Delete delete_android.
def delete_android(request,id):
    id=decrypt(id)
    abt_obj = Android.objects.filter(ad_id=id).delete()
    messages.warning(request, 'Record Deleted!!')
    return redirect('/dashboard/android/')


# android change action.
def android_change_action(request, objectId, state):
    objectId=decrypt(objectId)
    print(state, "==============state++++++++++++++++")
    obj = Android.objects.get(ad_id=objectId)
    if obj.action==True:
        print("somethingsssssssssssss")
        obj.action=False
        obj.save()
    else:
        print("something")
        obj.action=True
        obj.save()
    print(obj.action)    

    return HttpResponse('Action Changed!')    


def ios(request):
    obj_data = Ios.objects.values('ad_id','version','release_date','images','action')
    objs=[]
    for obj in obj_data:

        obj['encrypt_key']=encrypt(obj['ad_id'])
        obj['ad_id']=obj['ad_id']
        objs.append(obj)
    return render(request,'dashboard/ios.html',{'obj':objs})



# Add Publish blog.
def add_ios(request):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        file1 = file.get('images')
        # now = datetime.datetime.now().time()
        # merge_file = str(file1)+str(now)
        release_date = form.get('release_date')
        version = form.get('version')
        Ios.objects.create(version=version,release_date=release_date,images=file1)
        return redirect('/dashboard/ios/')
    else:
        return render(request,'dashboard/add_ios.html')


# Edit Publish blog.
def edit_ios(request,id):
    id=decrypt(id)
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        file1 = file.get('images')
        release_date = form.get('release_date')
        version = form.get('version')
        if file1:
            myfile = request.FILES['images']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            Ios.objects.filter(ad_id=id).update(version=version,release_date=release_date,images=filename) 
        obj = Ios.objects.filter(ad_id=id)

        Ios.objects.filter(ad_id=id).update(version=version,release_date=release_date)
        return redirect('/dashboard/ios/')
    else:
        obj = Ios.objects.filter(ad_id=id)

        return render(request,'dashboard/edit_ios.html',{'obj':obj})


# Delete delete_ios.
def delete_ios(request,id):
    id=decrypt(id)
    abt_obj = Ios.objects.filter(ad_id=id).delete()
    messages.warning(request, 'Record Deleted!!')
    return redirect('/career_blog/ios/')


# ios change action.
def ios_change_action(request, objectId, state):
    objectId=decrypt(objectId)
    print(state, "==============state++++++++++++++++")
    obj = Ios.objects.get(ad_id=objectId)
    if obj.action==True:
        print("somethingsssssssssssss")
        obj.action=False
        obj.save()
    else:
        print("something")
        obj.action=True
        obj.save()
    print(obj.action)    

    return HttpResponse('Action Changed!')    
import socket
socket.getaddrinfo('localhost', 8080)


def downloads(request):
    res = requests.get('http://127.0.0.1:8000/api/v1/download/')
    json_data = res.json()
    for data in json_data:
        m = data

        print(json_data,'fghjkjhgcavhbjkaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        print(m, 'pppppppppppppasssssworddddd')
    return render(request, 'dashboard/download.html',{'json_data':data})


def download_app(request):
    obj = DownloadApp.objects.all()
    return render(request,'dashboard/download_app.html',{'obj':obj})     

def download_app_change_action(request, objectId, state):
    print(state, "==============state++++++++++++++++")
    obj = DownloadApp.objects.get(d_id=objectId)
    if obj.action==True:
        print("somethingsssssssssssss")
        obj.action=False
        obj.save()
    else:
        subject = 'welcome to ADF world'
        html_message=render_to_string('dashboard/email.html',{'obj':obj})
        message=strip_tags(html_message)
        # message = f'Hi {obj.name}, thank you'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [obj.email_id, ]
        send_mail( subject, message, email_from, recipient_list )
        obj.action=True
        obj.save()
    print(obj.action)    

    return HttpResponse('Action Changed!')   


# https://mapi.adfpay.com/usersprofile/detail/
def user_profile(request):
    # obj = UserProfile.objects.all()
    res = requests.get('https://mapi.adfpay.com/usersprofile/detail/')
    print(res,'userdataaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    json_data = res.json()
    for item in json_data:
        print(item, 'pppppppppppppasssssworddddd')
    try:
        return render(request,'dashboard/user_profile.html',{'json_data': item})
    except:
        return redirect('/dashboard/')

def user_profile_change_action(request, objectId, state):
    print(state, "==============state++++++++++++++++")
    obj = UserProfile.objects.get(d_id=objectId)
    if obj.action==True:
        print("somethingsssssssssssss")
        obj.action=False
        obj.save()
    else:
        
        obj.action=True
        obj.save()
    print(obj.action)    

    return HttpResponse('Action Changed!')                  

def delete_user_profile(request,id):
    abt_obj = UserProfile.objects.filter(d_id=id).delete()
    messages.warning(request, 'Record Deleted!!')
    return redirect('/dashboard/user_profile/')

def online_user(request):
    res = requests.get('http://127.0.0.1:8000/api/v1/onlineuser/')
    json_data = res.json()
    for item in json_data:
        print(item,'pppppppppppppasssssworddddd')
    return render(request,'dashboard/online_user.html',{'json_data':item})


def restores(request):
    # obj = Restores.objects.all()
    res = requests.get('http://127.0.0.1:8000/api/v1/restore/')
    json_data = res.json()
    for item in json_data:
        print(item, 'pppppppppppppasssssworddddd')
    return render(request,'dashboard/restores.html',{'json_data':item})

def restores_change_action(request, objectId, state):
    print(state, "==============state++++++++++++++++")
    obj = Restores.objects.get(d_id=objectId)
    if obj.action==True:
        print("somethingsssssssssssss")
        obj.action=False
        obj.save()
    else:
        
        obj.action=True
        obj.save()
    print(obj.action)    

    return HttpResponse('Action Changed!')                  

def delete_restores(request,id):
    abt_obj = Restores.objects.filter(d_id=id).delete()
    messages.warning(request, 'Record Deleted!!')
    return redirect('/dashboard/user_profile/')    





def subscription(request):
    obj_data = Subscription.objects.values('d_id','country','profile_type','currency','amount','subscription_type','collection_method','action')
    objs=[]
    for obj in obj_data:

        obj['encrypt_key']=encrypt(obj['d_id'])
        obj['d_id']=obj['d_id']
        objs.append(obj)
    return render(request,'dashboard/subscription.html',{'obj':objs})



# Add Publish blog.
def add_subscription(request):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES    
        country = form.get('country')
        print(country,'countryfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
        currency = form.get('currency')
        amount = form.get('amount')
        profile_type = form.get('profile_type')
        subscription_type = form.get('subscription_type')
        collection_type = form.get('collection_type')
        Subscription.objects.create(country=country,profile_type=profile_type,currency=currency,amount=amount,subscription_type=subscription_type,collection_method=collection_type)
        return redirect('/dashboard/subscription/')
    else:
        return render(request,'dashboard/add_subscription.html')


# Edit Publish blog.
def edit_subscription(request,id):
    id=decrypt(id)

    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        country = form.get('country')
        currency = form.get('currency')
        amount = form.get('amount')
        profile_type = form.get('profile_type')
        subscription_type = form.get('subscription_type')
        collection_type = form.get('collection_type')
        
        
        obj = Subscription.objects.filter(d_id=id)

        Subscription.objects.filter(d_id=id).update(country=country,profile_type=profile_type,currency=currency,amount=amount,subscription_type=subscription_type,collection_method=collection_type)
        return redirect('/dashboard/subscription/')
    else:
        obj = Subscription.objects.filter(d_id=id)

        return render(request,'dashboard/edit_subscription.html',{'obj':obj})


# Delete delete_android.
def delete_subscription(request,id):
    id=decrypt(id)
    abt_obj = Subscription.objects.filter(d_id=id).delete()
    messages.warning(request, 'Record Deleted!!')
    return redirect('/dashboard/subscription/')


# Subscription change action.
def subscription_change_action(request, objectId, state):
    objectId=decrypt(objectId)
    print(state, "==============state++++++++++++++++")
    obj = Subscription.objects.get(d_id=objectId)
    if obj.action==True:
        print("somethingsssssssssssss")
        obj.action=False
        obj.save()
    else:
        print("something")
        obj.action=True
        obj.save()
    print(obj.action)    

    return HttpResponse('Action Changed!')      

def online_subscriber(request):
    # obj = OnlineSubscriber.objects.all()
    res = requests.get('http://127.0.0.1:8000/api/v1/subscribers/')
    json_data = res.json()
    for item in json_data:
        print(item, 'pppppppppppppasssssworddddd')
    return render(request,'dashboard/online_subscriber.html',{'json_data': item})

def online_subscriber_change_action(request, objectId, state):
    print(state, "==============state++++++++++++++++")
    obj = OnlineSubscriber.objects.get(d_id=objectId)
    if obj.action==True:
        print("somethingsssssssssssss")
        obj.action=False
        obj.save()
    else:
        
        obj.action=True
        obj.save()
    print(obj.action)    

    return HttpResponse('Action Changed!')              

def delete_online_subscriber(request,id):
    abt_obj = OnlineSubscriber.objects.filter(d_id=id).delete()
    messages.warning(request, 'Record Deleted!!')
    return redirect('/dashboard/online_subscriber/')    


def coupon_generate(request):
    # if request.method == 'POST':
    #     form = request.POST
    #     file = request.FILES
    #     country = form.get('country')
    #     profile_type = form.get('profile_type')
    #     discount_type = form.get('discount_type')
    #     discount_name = form.get('discount_name')
    #     amount = form.get('amount')
    #     issue_date = form.get('issue_date')
    #     valid_till = form.get('valid_to')
    #     coupon_number= form.get('coupon_number')
    #     status= form.get('status')
    #     abt_obj = Discount.objects.create(country=country, profile_type=profile_type, discount_type=discount_type,
    #                                       discount_name=discount_name, amount=amount, issue_date=issue_date,
    #                                       valid_till=valid_till,coupon_number=coupon_number,status=status)
    #     return redirect('coupon_listing')
    # else:
    res = requests.get('http://127.0.0.1:8000/api/v1/discount/')
    json_data = res.json()
    for item in json_data:
        print(item, 'pppppppppppppasssssworddddd')
    return render(request, 'dashboard/generate_discount_coupon.html', {'json_data': item})





def coupon_listing(request):
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")

    data = Discount.objects.all()
    for d in data:
        print(d.id,"hhhhhhhhhhhhhvg")
    print(data,'comming')

    return render(request,'dashboard/discount_coupon_listing.html',context={'data':data})

def coupon_expired(request):

    data = Discount.objects.filter(status='Expired')

    return render(request,'dashboard/discount_coupon_expired.html',context={'data':data})


def coupon_available(request):

    data = Discount.objects.filter(status='Active')

    return render(request,'dashboard/discount_coupon_available.html',context={'data':data})

def coupon_utilization(request):

    data = Discount.objects.filter(status='Active')

    return render(request,'dashboard/discount_coupon_utilisation.html',context={'data':data})



#pra
from partners.models import *

def pendingreg(request):
    context={}
    data = Becomepartner.objects.filter(status='pending')
    context={'data': data}
    return render(request,"dashboard/Badmin_templates/ref_application_received.html",context=context)


def declinereg(request):
    context={}
    data = Becomepartner.objects.filter(status='decline')
    context={'data': data}
    return render(request,'dashboard/Badmin_templates/decline_reg.html', context=context)


def view_approve(request):
    context={}
    data = Becomepartner.objects.filter(status='approve')

    context={'data': data}
    # return render(request,'Badmin_templates/view_reg.html',{'data':res})
    return render(request,"dashboard/Badmin_templates/ref_application_approved.html",context=context)



from partners.models import *


def approve_user(request):
    id = request.POST['a1']
    qs = Becomepartner.objects.filter(id=id)

    name = ""
    mobile = ""
    for x in qs:
        name = x.username
        mobile = x.mobile
        qs.update(status="approve")
        # mess = "Hello Mr/Miss : " + name + " Your Registration is Approved"
        # x=sendSMS(str(phone),mess)
        print(x)
    return redirect('pendingreg')


def decline_user(request):
    idno =request.POST['a2']
    qs = Becomepartner.objects.filter(id=idno)
    name=""
    phone=""
    for x in qs:
        name=x.username
        cno=x.mobile
        qs.update(status='decline')
        # mess= "Hello Mr/Miss : " + name + " Your Registration is Approved"
        # x=sendSMS(str(cno),mess)
    # return redirect('decline_reg')
    return render(request,'dashboard/Badmin_templates/decline_reg.html')

#priyanka

def logs(request):
    data = Evie_logs.objects.all()

    return render(request, 'dashboard/evie_logs.html', context={'data': data})

def all_mails(request):
    data = Mail.objects.all()

    return render(request, 'dashboard/mail_all.html', context={'data': data})

def mail_generate(request):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        country = form.get('country')
        state = form.get('state')
        city = form.get('city')
        client = form.get('client')
        mobile_no = form.get('mobile_no')
        email_id = form.get('email_id')
        service_name = form.get('service_name')
        mail_date= form.get('mail_date')
        mail_content= form.get('mail_content')
        ticket_id=form.get('ticket_id')
        date=form.get('date')
        allocated_to=form.get('allocated_to')
        allocated_date=form.get('allocated_date')
        status=form.get('status')
        action=form.get('action')
        abt_obj = Mail.objects.create(country=country, state=state, city=city,client=client, mobile_no=mobile_no, email_id=email_id,service_name=service_name,mail_date=mail_date,mail_content=mail_content, ticket_id=ticket_id,date=date,allocated_to=allocated_to,allocated_date=allocated_date,status=status,action=action)
        return redirect('all_mails')
    else:
        return render(request, 'dashboard/mail_generate.html')


def mail_resolved(request):
    data = Mail.objects.filter(status='Pending')

    return render(request, 'dashboard/mail_resolved.html', context={'data': data})

def mail_esclated(request):
    data = Mail.objects.all()

    return render(request, 'dashboard/mail_esclated.html', context={'data': data})

def mail_pending(request):
    data = Mail.objects.filter(status='Pending')

    return render(request, 'dashboard/mail_pending.html', context={'data': data})


def mail_expired(request):
    data = Mail.objects.filter(status='Expired')

    return render(request, 'dashboard/mail_expired.html', context={'data': data})


def new_mail_received(request):
    data = Mail.objects.filter(status='Pending')

    return render(request, 'dashboard/new_mail_received.html', context={'data': data})


def mail_forwarded(request):
    data = Mail.objects.filter(status='Pending')

    return render(request, 'dashboard/mail_forwarded.html', context={'data': data})
#tickets==================================

def ticket_generate(request):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        ticket_id=form.get('ticket_id')
        country = form.get('country')
        state = form.get('state')
        city = form.get('city')
        client = form.get('client')
        mobile_no = form.get('mobile_no')
        email_id = form.get('email_id')
        service_name = form.get('service_name')
        concern = form.get('concern')
        date = form.get('date')
        allocated_to=form.get('allocated_to')
        allocated_date=form.get('allocated_date')
        response_date = form.get('response_date')
        response_details = form.get('response_details')
        esclated_to= form.get('esclated_to')
        esclated_date= form.get('esclated_date')
        expired_on= form.get('expired_on')
        pending_since= form.get('pending_since')
        status=form.get('status')
        action=form.get('action')
        abt_obj = Ticket.objects.create(ticket_id=ticket_id,country=country, state=state, city=city,client=client, mobile_no=mobile_no, email_id=email_id,service_name=service_name,concern=concern,date=date,allocated_to=allocated_to,allocated_date=allocated_date,response_date=response_date,response_details=response_details,esclated_to=esclated_to,esclated_date=esclated_date,expired_on=expired_on,pending_since=pending_since,status=status,action=action)
        return redirect('all_tickets')
    else:
        return render(request, 'dashboard/ticket_generate.html')


def new_tickets(request):
    # data = Ticket.objects.filter(status='Pending')
    res = requests.get('http://127.0.0.1:8000/api/v1/ticket/')
    json_data = res.json()
    for item in json_data:
        print(item, 'pppppppppppppasssssworddddd')
    return render(request, 'dashboard/new_tickets.html', {'json_data': item})


def ticket_forwarded(request):
    data = Ticket.objects.filter(status='Pending')

    return render(request, 'dashboard/ticket_forwarded.html', context={'data': data})


def ticket_resolved(request):
    data = Ticket.objects.filter(status='Resolved')

    return render(request, 'dashboard/ticket_resolved.html', context={'data': data})


def ticket_esclated(request):
    data = Ticket.objects.filter(status='Pending')

    return render(request, 'dashboard/ticket_esclated.html', context={'data': data})


def ticket_pending(request):
    data = Ticket.objects.filter(status='Pending')

    return render(request, 'dashboard/ticket_pending.html', context={'data': data})

def ticket_expired(request):
    data = Ticket.objects.filter(status='Expired')

    return render(request, 'dashboard/ticket_expired.html', context={'data': data})

def all_tickets(request):
    data = Ticket.objects.filter()

    return render(request, 'dashboard/all_tickets.html', context={'data': data})

#chatbot========================================================================

def chatbot_generate(request):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        ticket_id=form.get('ticket_id')
        country = form.get('country')
        state = form.get('state')
        city = form.get('city')
        client = form.get('client')
        mobile_no = form.get('mobile_no')
        email_id = form.get('email_id')
        service_name = form.get('service_name')
        concern = form.get('concern')
        request_date = form.get('requestdate')
        request_contents= form.get('request_contents')
        date= form.get('date')
        allocated_to=form.get('allocated_to')
        allocated_date=form.get('allocated_date')
        response_date = form.get('response_date')
        response_details = form.get('response_details')
        esclated_to= form.get('esclated_to')
        esclated_date= form.get('esclated_date')
        expired_on= form.get('expired_on')
        pending_since= form.get('pending_since')
        solution_detail=form.get('solution_detail')
        solution_date=form.get('solution_date')
        status=form.get('status')
        action=form.get('action')
        abt_obj = ChatBot.objects.create(ticket_id=ticket_id,country=country, state=state, city=city,client=client,
                                        mobile_no=mobile_no, email_id=email_id,service_name=service_name,concern=concern,
                                        request_date=request_date,request_contents=request_contents,date=date,
                                        allocated_to=allocated_to,allocated_date=allocated_date,response_date=response_date,
                                        response_details=response_details,esclated_to=esclated_to,esclated_date=esclated_date,
                                        expired_on=expired_on,pending_since=pending_since,solution_detail=solution_detail,
                                        solution_date=solution_date,status=status,action=action)
        return redirect('all_request')
    else:
        return render(request, 'chatbot_generate.html')


def all_request(request):
    data = ChatBot.objects.filter()

    return render(request, 'dashboard/request_all.html', context={'data': data})

def request_pending(request):
    data = ChatBot.objects.filter(status='Pending')

    return render(request, 'dashboard/request_pending.html', context={'data': data})

def request_esclated(request):
    data = ChatBot.objects.filter(status='Pending')

    return render(request, 'dashboard/request_esclated.html', context={'data': data})

def request_resolved(request):
    data = ChatBot.objects.filter(status='Pending')

    return render(request, 'dashboard/request_resolved.html', context={'data': data})

def request_forwarded(request):
    data = ChatBot.objects.filter(status='Pending')

    return render(request, 'dashboard/request_forwarded.html', context={'data': data})

def request_expired(request):
    data = ChatBot.objects.filter(status='Expired')

    return render(request, 'dashboard/request_expired.html', context={'data': data})

def  new_request_received(request):
    # data = ChatBot.objects.filter(status='Pending')

    res = requests.get('http://127.0.0.1:8000/api/v1/chatbot/')
    json_data = res.json()
    for item in json_data:
        print(item, 'pppppppppppppasssssworddddd')

    return render(request, 'dashboard/new_request_received.html',{'json_data':item})
#phonecalls================================================

def calls_generate(request):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        ticket_id=form.get('ticket_id')
        country = form.get('country')
        state = form.get('state')
        city = form.get('city')
        client = form.get('client')
        mobile_no = form.get('mobile_no')
        email_id = form.get('email_id')
        service_name = form.get('service_name')
        call_date = form.get('call_date')
        call_contents = form.get('call_contents')
        concern = form.get('concern')
        request_date = form.get('request_date')
        request_contents= form.get('request_contents')
        date = form.get('date')
        allocated_to=form.get('allocated_to')
        allocated_date=form.get('allocated_date')
        response_date = form.get('response_date')
        response_details = form.get('response_details')
        esclated_to= form.get('esclated_to')
        esclated_date= form.get('esclated_date')
        expired_on= form.get('expired_on')
        pending_since= form.get('pending_since')
        solution_detail= form.get('solution_detail')
        solution_date= form.get('solution_date')
        status=form.get('status')
        action=form.get('action')
        abt_obj = PhoneConversation.objects.create(ticket_id=ticket_id,country=country, state=state, city=city,
                                        client=client, mobile_no=mobile_no, email_id=email_id, service_name=service_name, call_date=call_date, call_contents=call_contents, concern=concern, request_date=request_date,
                                        request_contents=request_contents,  date=date,allocated_to=allocated_to,allocated_date=allocated_date,
                                        response_date=response_date, response_details=response_details,esclated_to=esclated_to,
                                        esclated_date=esclated_date, expired_on=expired_on, pending_since=pending_since, solution_detail=solution_detail,
                                        solution_date=solution_date, status=status, action=action)
        return redirect('call_all')
    else:
        return render(request, 'dashboard/calls_generate.html')


def new_call_received(request):
    # data = PhoneConversation.objects.filter(status='Pending'
    res = requests.get('http://127.0.0.1:8000/api/v1/phoneconversation/')
    json_data = res.json()
    for item in json_data:
        print(item, 'pppppppppppppasssssworddddd')
    return render(request,'dashboard/new_call_received.html',{'json_data':item})



def new_call_forwarded(request):
    data = PhoneConversation.objects.filter(status='Pending')

    return render(request, 'dashboard/new_call_forwarded.html', context={'data': data})

def call_resolved(request):
    data = PhoneConversation.objects.filter(status='Pending')

    return render(request, 'dashboard/call_resolved.html', context={'data': data})


def call_esclated(request):
    data = PhoneConversation.objects.filter(status='Pending')

    return render(request, 'dashboard/call_esclated.html', context={'data': data})

def call_pending(request):
    data = PhoneConversation.objects.filter(status='Pending')

    return render(request, 'dashboard/call_pending.html', context={'data': data})

def call_all(request):
    data = PhoneConversation.objects.filter()

    return render(request, 'dashboard/call_all.html', context={'data': data})

#refer_and_earn
def incentive_structure(request):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        country = form.get('country')
        profile_type = form.get('profile_type')
        incentive_type = form.get('incentive_type')
        incentive_name = form.get('incentive_name')
        amount= form.get('amount')
        name= form.get('name')
        mobile_no = form.get('mobile_no')
        email_id = form.get('email_id')
        mode_of_payment= form.get('mode_of_payment')
        earned_on= form.get('earned_on')
        paid_on= form.get('paid_on')
        outstanding_since= form.get('outstanding_since')
        action=form.get('action')
        abt_obj = ReferAndEarn.objects.create(country=country,profile_type=profile_type,incentive_type=incentive_type,
                                      incentive_name=incentive_name,amount=amount,name=name,
                                      mobile_no=mobile_no, email_id=email_id,mode_of_payment=mode_of_payment,earned_on=earned_on,
                                      paid_on=paid_on,outstanding_since=outstanding_since,action=action)
        return redirect('incentive_utilised')
    else:
        return render(request, 'dashboard/incentive_structure.html')


def incentive_utilised(request):
    data = ReferAndEarn.objects.all()
    return render(request, 'dashboard/incentive_utilised.html', context={'data': data})

def incentive_paid(request):
    data = ReferAndEarn.objects.all()

    return render(request, 'dashboard/incentive_paid.html', context={'data': data})

def incentive_outstanding(request):
    data = ReferAndEarn.objects.all()
    return render(request, 'dashboard/incentive_outstanding.html', context={'data': data})


#community member

def become_application_received(request):
    context = {}
    data = BecomeMember.objects.filter(status='pending')
    context = {'data': data}
    return render(request, 'dashboard/banking_application_received.html', context=context)


def banking_application_approved(request):
    context = {}
    data = BecomeMember.objects.filter(status='approve')

    context = {'data': data}
    return render(request, 'dashboard/banking_application_approved.html',  context=context)

def banking_active_members(request):
    data = BecomeMember.objects.all()
    return render(request, 'dashboard/banking_active_members.html', context={'data': data})

def banking_members_performance(request):
    data = BecomeMember.objects.all()

    return render(request, 'dashboard/banking_members_performance.html', context={'data': data})

#payout structure
#def banking_members_payout_structure(request): #pending
 #   data = CommuityMember.objects.all()

  #  return render(request, 'banking_members_payout_structure.html', context={'data': data})

def banking_invoice_generated(request):
    data = CommuityMember.objects.all()

    return render(request, 'dashboard/banking_invoice_generated.html', context={'data': data})

def banking_invoice_approval(request):
    data = CommuityMember.objects.all()

    return render(request, 'dashboard/banking_invoice_approval.html', context={'data': data})

def banking_invoice_payment_status(request):
    data = CommuityMember.objects.all()

    return render(request, 'dashboard/banking_invoice_payment_status.html', context={'data': data})

# services

def service_listing(request):
    # data = Services.objects.all()
    res = requests.get('http://127.0.0.1:8000/api/v1/services/')
    json_data = res.json()
    for item in json_data:
        print(item, 'pppppppppppppasssssworddddd')
    # return render(request,'dashboard/download.html',{'json_data':item})

    return render(request, 'dashboard/service_listing.html', {'json_data':item})

def service_utilisation(request):
    data = Services.objects.all()

    return render(request, 'dashboard/service_utilisation.html', context={'data': data})

def service_charge_reciept(request):
    data = Services.objects.all()

    return render(request, 'dashboard/service_charge_reciept.html', context={'data': data})

def service_charge_outstanding(request):
    data = Services.objects.all()

    return render(request, 'dashboard/service_charge_outstanding.html', context={'data': data})

def service_charge_structure(request):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        country = form.get('country')
        profile_type = form.get('profile_type')
        service_type = form.get('service_type')
        service_name = form.get('service_name')
        service_charge = form.get('sevice_charge')
        gst_rate = form.get('gst_rate')
        gst_amount = form.get('gst_amount')
        total_charges = form.get('total_charges')
        action=form.get('action')
        abt_obj = Services.objects.create(country=country,profile_type=profile_type,
                                              service_type=service_type,service_name=service_name,service_charge=service_charge,
                                              gst_rate=gst_rate,gst_amount=gst_amount,total_charges=total_charges,action=action)
        return redirect('service_listing')
    else:
        return render(request, 'dashboard/service_charge_structure.html')

#Transaction History
def transaction_initiated(request):
    # data = TransactionHistory.objects.all()
    res = requests.get('http://127.0.0.1:8000/api/v1/transactionhistory/')
    json_data = res.json()
    for item in json_data:
        print(item, 'pppppppppppppasssssworddddd')
    return render(request, 'dashboard/transaction_initiated.html', {'json_data': item})

def transaction_completed(request):
    data = TransactionHistory.objects.all()
    return render(request, 'dashboard/transaction_completed.html', context={'data': data})

def transaction_pending(request):
    data = TransactionHistory.objects.all()
    return render(request, 'dashboard/transaction_pending.html', context={'data': data})

def transaction_failed(request):
    data = TransactionHistory.objects.all()
    return render(request, 'dashboard/transaction_failed.html', context={'data': data})


def partner_structure(request):
    data = PartnerPayoutStructure.objects.all()
    return render(request, 'dashboard/Badmin_templates/ref_members_payout_structure.html', context={'data': data})

def partner_save(request):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        country = form.get('country')
        state = form.get('state')
        city = form.get('city')
        name = form.get('name')
        mobile = form.get('mobile')
        email = form.get('email')
        active = form.get('active')
        range = form.get('range')
        currency=form.get('currency')
        rate = form.get('rate')
        startdate = form.get('startdate')
        valid = form.get('valid')
        abt_obj = PartnerPayoutStructure.objects.create(country=country,state=state,city=city,name=name,mobile=mobile,
                                                        email=email,active_since=active,user_range=range,payout_rate=rate,
                                                        currency=currency,start_date=startdate,valid_till_date=valid)
        return redirect('partner_structure')
    else:
        return render(request, 'dashboard/Badmin_templates/ref_members_payout_structure.html')


def active_user(request):
    data = Becomepartner.objects.filter(status='active')
    return render(request, 'dashboard/Badmin_templates/ref_active_members.html', context={'data': data})


def member_perfomance(request):
    return render(request, 'dashboard/Badmin_templates/ref_members_performance.html')


def invoice_generate(request):
    return render(request, 'dashboard/Badmin_templates/ref_invoice_generated.html')


def invoice_approval(request):
    return render(request, 'dashboard/Badmin_templates/ref_invoice_approval.html')


def invoice_payment(request):
    return render(request, 'dashboard/Badmin_templates/ref_invoice_payment_status.html')


def approve_member(request):
    id = request.POST['a2']
    qs = BecomeMember.objects.filter(id=id)


    name = ""
    mobile = ""

    for x in qs:
        name = x.full_name
        mobile = x.mobile
        qs.update(status="approve")
        # mess = "Hello Mr/Miss : " + name + " Your Registration is Approved"
        # x=sendSMS(str(phone),mess)
    return redirect('banking_application_approved')


def internal_user_list(request):
    noEntry = True
    objectList = []
    fieldNames = []
    totalObjectList = []
    totalFieldNames = []
    objectType = "InternalUsers"
    objList = getDBObject(objectType, 'showObjectList')
    if objList:
        noEntry, fieldNames, objectList = return_object_list(objList)
    context = {
        "noEntry": noEntry,
        "objects": objectList,
        "objectType": objectType,
        "displayObjectType": putSpace(objectType),
        "fieldNames": fieldNames,
        "totalobjects": totalObjectList,
        "totalFieldNames": totalFieldNames,
    }
    return render(request, 'dashboard/internal_user_list.html', context=context)


def create_internal_user(request):
    response = requests.get('https://mapi.adfpay.com/usersprofile/detail/')
    data = response.json()
    country_list = []
    city_list = []
    user_profile_list = []
    for i in data:
        country_list.append(i['country'])
        city_list.append(i['city'])
        user_profile_list.append(i['user_type'])

    # country = list(set(country_list))
    # city = list(set(city_list))
    # profile_type = list(set(user_profile_list))
    country = [x for x in list(set(country_list)) if x is not None]
    city = [x for x in list(set(city_list)) if x is not None]
    profile_type = [x for x in list(set(user_profile_list)) if x is not None]
    menu_data = PermissionMenu.objects.filter(status=1).order_by('id')
    mylist = []
    for menu in menu_data:
        mydict = {}
        menu_submenu_data = PermissionSubMenu.objects.filter(status=1, menu_id__status=1, menu_id=menu.id)
        submenu_list = []
        for sub in menu_submenu_data:
            submenu_dict = {}
            submenu_dict['id'] = sub.id
            submenu_dict['permission_sub_menu'] = sub.permission_sub_menu
            submenu_list.append(submenu_dict)
        mydict[menu.permission_menu] = submenu_list
        mylist.append(mydict)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_no = request.POST.get("phone_no")
        designation = request.POST.get("designation")
        password = request.POST.get("password")
        country = request.POST.get("country")
        city = request.POST.get("city")
        profile_type = request.POST.get("profile_type")
        function_names = request.POST.getlist("function_names[]")
        permission_types = request.POST.getlist("permission_types")
        action = 'Active'
        username = email.split('@')[0]
        print(function_names)
        try:
            if User.objects.get(email=email) or User.objects.get(username=username):
                messages.warning(request, 'Email Id already exists!')
                return render(request, "dashboard/internal_user.html", context={'operation': 'create'})
        except Exception as e:
            print("Email Id doesn't exists!")
        user = User.objects.create_user(username=username, email=email, password=password, is_staff=True)
        users = InternalUsers(user_id=user.id, name=name, email=email, password=password, phone_no=phone_no,
                              designation=designation)
        users.save()
        from_email = settings.EMAIL_HOST_USER
        subject = 'Account Created, Get Your Account Details Here! - Neobank'
        html_message = render_to_string('accounts/account_created.html',
                                        context={'name': name, 'username': username, 'email': email,
                                                 'password': password})
        plain_message = strip_tags(html_message)
        try:
            send_mail(subject=subject, message=plain_message, from_email=from_email, recipient_list=[email],
                      html_message=html_message)
        except:
            pass
            # return HttpResponse('Invalid header found.')
        messages.success(request, 'Account Created Successfully! Check your email for the password details.')
        return redirect('internal_user_list')
    return render(request, "dashboard/internal_user.html",
                  context={'operation': 'create', 'country': country, 'city': city, 'profile_type': profile_type,
                           'permissions': mylist})


def update_internal_user(request, id):
    response = requests.get('https://mapi.adfpay.com/usersprofile/detail/')
    data = response.json()
    country_list = []
    city_list = []
    user_profile_list = []
    for i in data:
        country_list.append(i['country'])
        city_list.append(i['city'])
        user_profile_list.append(i['user_type'])

    # country = list(set(country_list))
    # city = list(set(city_list))
    # profile_type = list(set(user_profile_list))
    country = [x for x in list(set(country_list)) if x is not None]
    city = [x for x in list(set(city_list)) if x is not None]
    profile_type = [x for x in list(set(user_profile_list)) if x is not None]
    objectToUpdate = InternalUsers.objects.filter(id=id).values()[0]
    citylist = objectToUpdate['city']
    countrylist = objectToUpdate['country']
    profile_typelist = objectToUpdate['profile_type']
    function_names_list = eval(objectToUpdate['function_names'])
    permission_types_list = eval(objectToUpdate['permission_types'])

    menu_data = PermissionMenu.objects.filter(status=1).order_by('id')
    mylist = []
    for menu in menu_data:
        mydict = {}
        menu_submenu_data = PermissionSubMenu.objects.filter(status=1, menu_id__status=1, menu_id=menu.id)
        submenu_list = []
        for sub in menu_submenu_data:
            submenu_dict = {}
            submenu_dict['id'] = sub.id
            submenu_dict['permission_sub_menu'] = sub.permission_sub_menu
            submenu_list.append(submenu_dict)
        mydict[menu.permission_menu] = submenu_list
        mylist.append(mydict)
    intuser = InternalUsers.objects.get(id=id)
    if request.method == "POST":
        function_names = request.POST.getlist('function_names[]')
        objToUpdate = InternalUsers.objects.get(id=id)
        user = User.objects.get(id=objToUpdate.user_id)
        for key in request.POST:
            if len(request.POST[key]) != 0 and key != 'csrfmiddlewaretoken':
                if key == 'function_names[]':
                    setattr(objToUpdate, 'function_names', request.POST.getlist(key))
                if key == 'permission_types':
                    setattr(objToUpdate, key, request.POST.getlist(key))
                elif key == 'email':
                    email = request.POST[key]
                    username = email.split('@')[0]
                    setattr(objToUpdate, key, request.POST[key])
                    user.email = email
                    user.username = username
                    user.save()
                elif key == 'password':
                    setattr(objToUpdate, key, request.POST[key])
                    user.password = request.POST['password']
                    user.set_password(user.password)
                    user.save()
                else:
                    setattr(objToUpdate, key, request.POST[key])
        objToUpdate.save()
        messages.success(request, 'Account Updated Successfully!')
        return redirect('internal_user_list')
    return render(request, "dashboard/internal_user.html",
                  context={'countrylist': countrylist, 'citylist': citylist, 'profile_typelist': profile_typelist,
                           'id': id, 'objects': objectToUpdate, 'function_names_list': function_names_list,
                           'permission_types_list': permission_types_list, 'country': country, 'city': city,
                           'profile_type': profile_type, 'permissions': mylist})


def access_and_permisiion(request):
    noEntry = True
    objectList = []
    fieldNames = []
    totalObjectList = []
    totalFieldNames = []
    objectType = "InternalUsers"
    objList = getDBObject(objectType, 'showObjectList')
    if objList:
        noEntry, fieldNames, objectList = return_object_list(objList)
    context = {
        "noEntry": noEntry,
        "objects": objectList,
        "objectType": objectType,
        "displayObjectType": putSpace(objectType),
        "fieldNames": fieldNames,
        "totalobjects": totalObjectList,
        "totalFieldNames": totalFieldNames,
    }
    return render(request, 'dashboard/internal_user_list.html', context=context)


def internal_user(request):
    return render(request, 'dashboard/internal_user.html')


