from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import inspect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from api.models import *
from accounts.models import *
import api.models as models 
from django.urls import reverse
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from .reports import *
import re
from api.forms import *
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test

modelNames = list()
modelNames.append('UserProfilesAndroid')
modelNames.append('UserProfilesIOS')
modelNames.append('InternalUsers')
for name, obj in inspect.getmembers(models, inspect.isclass):
   modelNames.append(name)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    context = {
        'vacancy_report' : VacancyReport(),
        'resume_receipt_report' : ResumeReceiptReport(),
        'downloads_report' : DownloadsReport(),
        'online_users_report' : OnlineUsersReport(),
        'user_profiles_report' : UserProfilesReport(),
        'backup_report' : BackupReport(),
        'restore_report' : RestoreReport(),
        'feedback_report' : FeedbackReport(),
        'reviews_report' : ReviewsReport(),
        'subscription_report' : SubscriptionReport()
    }
    return render(request, 'neoadmin/dashboard.html', context = context)
def permission(request):
    context = {
        # 'vacancy_report' : VacancyReport(),
        # 'resume_receipt_report' : ResumeReceiptReport(),
        # 'downloads_report' : DownloadsReport(),
        # 'online_users_report' : OnlineUsersReport(),
        # 'user_profiles_report' : UserProfilesReport(),
        # 'backup_report' : BackupReport(),
        # 'restore_report' : RestoreReport(),
        # 'feedback_report' : FeedbackReport(),
        # 'reviews_report' : ReviewsReport(),
        # 'subscription_report' : SubscriptionReport()
    }
    return render(request, 'neoadmin/permission.html', context=context)


def permission_users(request):
    context = {
        # 'vacancy_report' : VacancyReport(),
        # 'resume_receipt_report' : ResumeReceiptReport(),
        # 'downloads_report' : DownloadsReport(),
        # 'online_users_report' : OnlineUsersReport(),
        # 'user_profiles_report' : UserProfilesReport(),
        # 'backup_report' : BackupReport(),
        # 'restore_report' : RestoreReport(),
        # 'feedback_report' : FeedbackReport(),
        # 'reviews_report' : ReviewsReport(),
        # 'subscription_report' : SubscriptionReport()
    }
    return render(request, 'neoadmin/permission_users.html', context=context)
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

def save_downloads_count(objectType):
    if objectType == 'TotalDownloadsAndroid':
        total_downloads = TotalDownloadsAndroid.objects.all()
        for entry in total_downloads:
            count_single_downloads = SingleDownloadAndroid.objects.filter(regionid=entry.id).count()
            entry.counting = count_single_downloads
            entry.save()
    elif objectType == 'TotalDownloadsIOS':
        total_downloads = TotalDownloadsIOS.objects.all()
        for entry in total_downloads:
            count_single_downloads = SingleDownloadIOS.objects.filter(regionid=entry.id).count()
            entry.counting = count_single_downloads
            entry.save()

def putSpace(input):
    words = re.findall('[A-Z][a-z]*', input)
    result = []
    for word in words:
        word = chr( ord (word[0]) + 32) + word[1:]
        result.append(word)
    return ' '.join(result).title()

@login_required
def show_object_list(request, objectType):
    if not check_user_functions(request, objectType):
        messages.error(request, 'You are not allowed to view {} model!'.format(objectType))
        return redirect('dashboard')
    noEntry = True
    objectList = []
    fieldNames = []
    totalObjectList = []
    totalFieldNames = []

    if objectType == 'TotalDownloadsAndroid':
        objList = getDBObject('SingleDownloadAndroid','showObjectList')
        objList2 = getDBObject('TotalDownloadsAndroid','showObjectList')
        save_downloads_count(objectType)
        if objList2:
            noEntry, totalFieldNames, totalObjectList = return_object_list(objList2)
    elif objectType == 'TotalDownloadsIOS':
        objList = getDBObject('SingleDownloadIOS','showObjectList')
        objList2 = getDBObject('TotalDownloadsIOS','showObjectList')
        save_downloads_count(objectType)
        if objList2:
            noEntry, totalFieldNames, totalObjectList = return_object_list(objList2)
    else:
        objList = getDBObject(objectType,'showObjectList')

    if objList:
        noEntry, fieldNames, objectList = return_object_list(objList)

    context = {
        "noEntry":noEntry,
        "objects": objectList,
        "objectType": objectType,
        "displayObjectType": putSpace(objectType),
        "fieldNames": fieldNames,
        "totalobjects": totalObjectList,
        "totalFieldNames" : totalFieldNames,
    }

    return render(request, 'neoadmin/show_object_list.html', context = context)

@login_required
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
        templateFile = 'neoadmin/adminforms/'+objectType+'Form.html'
        return render(request,templateFile, context)

@csrf_exempt
def saveObject(request, objectType):
    ckeditor_list = ['PublishBlogs', 'ManageNewsMedia', 'TermsAndConditions', 'TermsOfUse', 'FairPracticeCode', 'PrivacyPolicy', 'Disclaimer', 'GrievanceAddressMechanism', 'Faq', 'LifeAtAdfpay']
    if not check_user_functions(request, objectType):
        messages.error(request, 'You are not allowed to create entry to this {} model!'.format(objectType))
        return redirect('dashboard')
    if request.POST:
        if not check_permission_types(request, 'create'):
            messages.error(request, 'You do not have create access!')
            return redirect('dashboard')
        objToSave = getDBObject(objectType,'saveObject')
        for key in request.POST:
            if key != 'csrfmiddlewaretoken' and len(request.POST[key]) != 0:
                if key == 'content' and objectType in ckeditor_list:
                    objectTypeForm = objectType + 'Form'
                    form = getFormClass(request, objectTypeForm, 'saveform')
                    if form.is_valid():
                        content = form.cleaned_data['content']
                        setattr(objToSave,'content',content)
                else:
                    new_value = request.POST[key].replace('\r', '<br>').replace('\n', '<br>')
                    setattr(objToSave,key,new_value)
        for key in request.FILES:
            file_instance = request.FILES[key]
            tempFileName = objectType+'_'+datetime.now().strftime("%m%d%y%H%M%S")+'.'+str(request.FILES[key]).split('.')[-1]
            fs = FileSystemStorage()
            filename = fs.save(tempFileName, file_instance)
            uploaded_file_url = fs.url(filename)
            setattr(objToSave,key,uploaded_file_url)

        objToSave.save()

        context = {
        "objectType":objectType,
        "objectID":objToSave.id,
        "Operation":'add',
        }
        messages.success(request, 'Record Saved!')
        return redirect('show_object_list', objectType=objectType)

@csrf_exempt
def updateObject(request,objectType,objectId):
    ckeditor_list = ['PublishBlogs', 'ManageNewsMedia','TermsAndConditions', 'TermsOfUse', 'FairPracticeCode', 'PrivacyPolicy', 'Disclaimer', 'GrievanceAddressMechanism', 'Faq', 'LifeAtAdfpay']
    if not check_user_functions(request, objectType):
        messages.error(request, 'You are not allowed to update entry of this {} model!'.format(objectType))
        return redirect('dashboard')
    if request.POST:
        if not check_permission_types(request, 'update'):
            messages.error(request, 'You do not have update access!')
            return redirect('dashboard')
        objToUpdate = getDBObject(objectType,'updateObject',objectId)
        for key in request.POST:
            if len(request.POST[key]) != 0:
                if key == 'content' and objectType in ckeditor_list:
                    objectTypeForm = objectType + 'Form'
                    form = getFormClass(request, objectTypeForm, 'saveform')
                    if form.is_valid():
                        content = form.cleaned_data['content']
                        setattr(objToUpdate,'content',content)
                else:
                    new_value = request.POST[key].replace('\r', '<br>').replace('\n', '<br>')
                    setattr(objToUpdate,key,new_value)

        for key in request.FILES:
            file_instance = request.FILES[key]
            tempFileName = objectType+'_'+datetime.now().strftime("%m%d%y%H%M%S")+'.'+str(request.FILES[key]).split('.')[-1]
            fs = FileSystemStorage()
            filename = fs.save(tempFileName, file_instance)
            uploaded_file_url = fs.url(filename)
            setattr(objToUpdate,key,uploaded_file_url)

        objToUpdate.save()

        context = {
        "objectType":objectType,
        "objectID":objToUpdate.id,
        "Operation":'update',
        }
        messages.success(request, 'Record Updated!')
        return redirect('show_object_list', objectType=objectType)

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
    return redirect('show_object_list', objectType=objectType)

def test(request):
    print(request)

    for key in request.POST:
        if len(request.POST[key]) != 0:
            print(key, request.POST[key])

    for key in request.FILES:
        print(key, request.FILES[key])

    return render(request, "neoadmin/test.html", context = {})
