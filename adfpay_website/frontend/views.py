from django.shortcuts import render, redirect
from api.models import *
from .web_content import *
from datetime import datetime
from django.core.files.storage import FileSystemStorage
import re
from django.contrib import messages
from .templatetags import menu_helper
from dashboard.models import *
from partners.models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.conf import settings
from .encryption_util import *
# Create your views here.

def return_object_list(objList):
    objectList = list()
    for singleObject in objList:
        obj = dict()
        for key in singleObject:
            new_key = key.replace('_', ' ').title(
            ) if key != 'id' else 'Process Names' if key == 'function_names' else 'id'
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


def basic_setup():
    navmenu_list = navmenu()
    footer_logo, footer_description, google_play_store_link, facebook_page_link, twitter_page_link, pinterest_page_link, linkedin_page_link = footer()
    partners_list = partners()
    header_logo, header_title, header_description, google_play_store_link = header()

    context = {
        'header_logo': header_logo,
        'header_title': header_title,
        'header_description': header_description,
        'google_play_store_link': google_play_store_link,
        'navmenu_list': navmenu_list,
        'footer_logo': footer_logo,
        'footer_description': footer_description,
        'facebook_page_link': facebook_page_link,
        'twitter_page_link': twitter_page_link,
        'pinterest_page_link': pinterest_page_link,
        'linkedin_page_link': linkedin_page_link,
        'partners_list': partners_list,
    }
    return context

def add_country_code(request):
    if request.method == 'POST':
        context={}
        form = request.POST
       
        country_code = form.get('country_code')
        phone = form.get('phone')
        CountryCode.objects.create(countrycode=country_code,mobile=phone)
        messages.success(request, "Thanks for downloading app, link has been sent on your mobile , please download app.")
        return render(request, 'frontend/index.html', context=context)
    else:
        return render(request,'frontend/base.html')

from phonenumbers import COUNTRY_CODE_TO_REGION_CODE
from django.contrib.gis.geoip2 import GeoIP2
def index(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('index')
    testimonials_list = testimonials()
    print(testimonials_list)
    services_dict = services_list()
    context['seo_title'] = seo_title
    context['seo_description'] = seo_description
    context['testimonials_list'] = testimonials_list
    context['services_dict'] = services_dict
    g = GeoIP2()
    ip = request.META.get('REMOTE_ADDR', None)
    # print(ip)
    # code=None
    new_code=None
    if not ip == "127.0.0.1":
        codess = g.city(ip)['country_code']
        codes=codess.upper()
        print('1#############')
        for code, isos in COUNTRY_CODE_TO_REGION_CODE.items():
            if codes in isos:
                print('2#############',code)
                new_code=code
    context={
        'new_code':new_code,
    }          
    return render(request, 'frontend/index.html', context)


def about(request, *args, **kwargs):
    context = {}
    # context = basic_setup()
    # seo_title, seo_description = manage_seo_content('about')
    # about_heading, about_content, vision, mission = about_us()
    # context['seo_title'] = seo_title
    # context['seo_description'] = seo_description
    # context['about_heading'] = about_heading
    # context['about_content'] = about_content
    # context['vision'] = vision
    # context['mission'] = mission
    data = AboutUs.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'frontend/aboutus.html', context)





def employees(request, *args, **kwargs):
    context = {}
    # seo_title, seo_description = manage_seo_content('sign_in')
    
    data = Product.objects.values('id','productname','upload','heading1','content1','content2','heading2','content3','heading3','content4','four_steps','step1heading','step1content','step2heading','step2content','step3heading','step3content','step4heading','step4content','eligibility_content','criteria1','criteria2','criteria3','criteria4','action')
    objs=[]
    for obj in data:

        obj['encrypt_key']=encrypt(obj['id'])
        obj['id']=obj['id']
        objs.append(obj)
    p=Paginator(objs,4)
    page_number=request.GET.get('page')
    page_obj=p.get_page(page_number)
    return render(request, 'frontend/employees.html', {'page_obj':page_obj})


def retailer(request, *args, **kwargs):
    # seo_title, seo_description = manage_seo_content('sign_in')
    data = Retailer.objects.values('id','retailername','upload','heading1','content1','content2','heading2','content3','heading3','content4','four_steps','step1heading','step1content','step2heading','step2content','step3heading','step3content','step4heading','step4content','eligibility_content','criteria1','criteria2','criteria3','criteria4','action')
    objs=[]
    for obj in data:

        obj['encrypt_key']=encrypt(obj['id'])
        obj['id']=obj['id']
        objs.append(obj)
    p=Paginator(objs,4)
    page_number=request.GET.get('page')
    page_obj=p.get_page(page_number)
    return render(request, 'frontend/retailer.html', {'page_obj':page_obj})


def profession(request, *args, **kwargs):
    # seo_title, seo_description = manage_seo_content('sign_in')
    data = Professional.objects.values('id','professionalname','upload','heading1','content1','content2','heading2','content3','heading3','content4','four_steps','step1heading','step1content','step2heading','step2content','step3heading','step3content','step4heading','step4content','eligibility_content','criteria1','criteria2','criteria3','criteria4','action')
    objs=[]
    for obj in data:

        obj['encrypt_key']=encrypt(obj['id'])
        obj['id']=obj['id']
        objs.append(obj)
    p=Paginator(objs,4)
    page_number=request.GET.get('page')
    page_obj=p.get_page(page_number)
    return render(request, 'frontend/profession.html',{'page_obj':page_obj})


def profession_detail(request,id):
    context = {}
    id=decrypt(id)
    # seo_title, seo_description = manage_seo_content('sign_in')
    data = Professional.objects.get(id=id)
    context = {
        'data': data,
    }
    return render(request, 'frontend/profession_detail.html', context=context)


def employees_details(request,id):
    context = {}
    # seo_title, seo_description = manage_seo_content('sign_in')
    id=decrypt(id)
    data = Product.objects.get(id=id)
    context = {
        'data': data,
    }
    return render(request, 'frontend/employee_detail.html', context=context)

def retailer_details(request,id):
    context = {}
    id=decrypt(id)
    # seo_title, seo_description = manage_seo_content('sign_in')
    data = Retailer.objects.get(id=id)
    context = {
        'data': data,
    }
    return render(request, 'frontend/retailer_detail.html', context=context)


def partner_login(request, *args, **kwargs):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('countheader'))
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user_object = User.objects.get(username=email)
        username = user_object.username
        user = authenticate(request, username=username, password=password)
        try:
            user3=Becomepartner.objects.get(email=email)
            partner=user3.is_partner
        except Becomepartner.DoesNotExist:
            messages.warning(request, 'No Partner Account')
            return render(request, 'frontend/partner_login.html', context = {})
        finally :
            if user.is_staff:
                login(request, user)
                return HttpResponseRedirect(reverse('countheader'))

        if user is not None and user.is_staff:
            login(request, user)
            return HttpResponseRedirect(reverse('countheader'))

        elif user is not None and partner:
            login(request, user)
            return HttpResponseRedirect(reverse('countheader'))
        
        elif user3 is None:
            messages.warning(request, 'User exists but have no partner access!')
            return render(request, 'frontend/partner_login.html', context = {})

        elif user is not None and partner is not True:
            messages.warning(request, 'User exists but have no partner access!')
            return render(request, 'frontend/partner_login.html', context = {})
        else:
            messages.error(request, 'Invalid Login Credentials!')
            return render(request, 'frontend/partner_login.html', context = {})
    return render(request, 'frontend/partner_login.html', context = {})


def become_partner(request, *args, **kwargs):
    context={}
    # if request.method=="POST":
        
    #     form = request.POST
    #     photo = request.FILES
    #     photo = photo.get('photo')
    #     print(photo)
    #     username=form.get('username')
    #     mobile = form.get('mobile')
    #     email = form.get('email')
    #     residential_address = form.get('residential_adddress')
    #     locality = form.get('locality')
    #     country= form.get('country')
    #     state=form.get('state')
    #     city = form.get('city')
    #     User.objects.create(username=username,mobile=mobile,photo=photo,email=email,residential_address=residential_address,locality=locality,country=country,state=state,city=city,is_partner=True)
    #     print(User)
    #     messages.success(request, "Added Successfully")
    return render(request, 'frontend/becomepartner.html', context=context)
    # else:
    #     return render(request, 'frontend/becomepartner.html', context=context)
    


def download_app(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('download_app')
    # context={}
    if request.method=="POST":
        form=request.POST
        full_name=form.get('fullname')
        email=form.get('email')
        mobile=form.get('mobile')
        print("jjjjjjjjjjjjjjj")
        print(DownloadApp.objects.all())
        att_obj=DownloadApp.objects.create(name=full_name,phonenumber=mobile,email_id=email)
        print(att_obj.phonenumber)

        messages.success(request, "Thank you for Downloading app,  link to download app has been sent on your email id, please download app from there")
        return render(request, 'frontend/download-app.html', context=context)
    else:    

        return render(request, 'frontend/download-app.html', context=context)


def sign_in_download(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('sign_in_download')
    return render(request, 'frontend/sign-in-download.html', context=context)
    

def sign_in(request, *args, **kwargs):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('cugdashboard'))
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user_object = User.objects.get(username=email)
        username = user_object.username
        user = authenticate(request,username=username, password=password)
        try:
            user2=BecomeMember.objects.get(email=email)
            member=user2.is_member
        
        except BecomeMember.DoesNotExist:
            messages.warning(request, 'No Community Account')
            return render(request, 'frontend/sign-in.html', context = {})
        finally :
            if user.is_staff:
                login(request, user)
                return HttpResponseRedirect(reverse('cugdashboard'))
        if user is not None and member:
            login(request, user)
            return HttpResponseRedirect(reverse('cugdashboard'))
        elif user is not None and user.is_staff:
            login(request, user)
            return HttpResponseRedirect(reverse('cugdashboard'))
        elif user is not None and member is not True:
            messages.warning(request, 'User exists but have no community access!')
            return render(request, 'frontend/sign-in.html', context = {})
        else:
            messages.error(request, 'Invalid Login Credentials!')
            return render(request, 'frontend/sign-in.html', context = {})
    return render(request, 'frontend/sign-in.html', context = {})
    


def sign_up(request, *args, **kwargs):
    context={}

    return render(request, 'frontend/sign-up.html',context=context)
    # else:
    #     return render(request, 'frontend/sign-up.html', context=context)



def blog(request, *args, **kwargs):
    
    
    # country_name=g.country('country_name')
    # print(country_name,g.country('google.com'))
    obj_data = PublishBlogs.objects.values('id','publisher_name','frontend_show','topic','image','content','published_date','action')
    objs=[]
    for obj in obj_data:

        obj['encrypt_key']=encrypt(obj['id'])
        obj['id']=obj['id']
        objs.append(obj)
   
    p = Paginator(objs, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'obj_data': page_obj}
    # sending the page object to index.html

    
    return render(request, 'frontend/blog.html',context)


def blog_detail(request,id):
    id=decrypt(id)
    obj_data = PublishBlogs.objects.get(id=id)
    

    return render(request, 'frontend/blog-detail.html', {'obj':obj_data})
# def blog_detail(request, id):
#     context = basic_setup()
#     blog_publisher_name, blog_topic, blog_image, blog_contents, blog_published_date = blog_details(
#         id)
#     blog_list = blog_objects()
#     context['seo_title'] = blog_topic + ' - Neo Blogs'
#     context['seo_description'] = blog_contents
#     if blog_list:
#         context['blog_list'] = blog_list[0:2]
#     context['blog_publisher_name'] = blog_publisher_name
#     context['blog_topic'] = blog_topic
#     context['blog_image'] = blog_image
#     context['blog_contents'] = blog_contents
#     context['blog_published_date'] = blog_published_date
#     return render(request, 'frontend/blog-detail.html', context=context)


def contact(request, *args, **kwargs):
    context = basic_setup()
    contact_email, contact_phone_no, contact_address = contact_us()
    seo_title, seo_description = manage_seo_content('contact')
    context['contact_email'] = contact_email
    context['contact_phone_no'] = contact_phone_no
    context['contact_address'] = contact_address
    context['seo_title'] = seo_title
    context['seo_description'] = seo_description
    return render(request, 'frontend/contact-us.html', context=context)


# def news_event(request, *args, **kwargs):
#     context = basic_setup()
#     seo_title, seo_description = manage_seo_content('news_event')
#     news_media_list = manage_news_media()
#     context['seo_title'] = seo_title
#     context['seo_description'] = seo_description
#     context['news_media_list'] = news_media_list
#     if news_media_list:
#         context['latest_news'] = reversed(news_media_list[0:2])
#     return render(request, 'frontend/news-event.html', context=context)
# def news_objects():

#     news_objects = ManageNewsMedia.objects.filter(action = 'Active').order_by('published_date')
#     news_list, count, dual_count = [], -1, 0
#     for news in news_objects:
#         if dual_count % 2 == 0:
#             news_list.append([])
#             count = count + 1
#         news_list[count].append(news.id)
#         news_list[count].append(news.topic)
#         news_list[count].append(news.media_file)
#         news_list[count].append(news.publisher_name)
#         news_list[count].append(news.published_date)
#         if len(news.content) > 160:
#             news_list[count].append(news.content[0:160] + '...')
#         else:
#             news_list[count].append(news.content)
#         dual_count = dual_count + 1
#     return news_list

def news_event(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('news')
    news_list = news_objects()
    paginator = Paginator(news_list, 2)
    page = request.GET.get('page', 1)
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        news_list = paginator.page(1)
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)

    context['seo_title'] = seo_title
    context['seo_description'] = seo_description
    context['news_list'] = news_list
    context['page']= page
    if news_list:
        context['latest_blogs'] = reversed(news_list[0:2])
    return render(request, 'frontend/news-event.html', context=context)


def news_event_detail(request, id):
    context = basic_setup()
    news_publisher_name, news_topic, news_image, news_contents, news_published_date = news_details(
        id)
    news_list = news_objects()
    newsids = ManageNewsMedia.objects.filter(action='Active').values_list('id', flat=True)
    context['seo_title'] = news_topic
    context['seo_description'] = news_contents
    if news_list:
        context['blog_list'] = news_list[0:2]
    context['news_publisher_name'] = news_publisher_name
    context['news_topic'] = news_topic
    context['news_image']= news_image
    context['news_contents'] = news_contents
    context['news_published_date'] = news_published_date
    return render(request, 'frontend/news-event-detail.html', context=context)

# def news_event_detail(request, id):
#     context = basic_setup()
#     news_media_topic, news_media_media_file, news_media_contents, news_media_published_date = news_media_detail(
#         id)
#     news_media_list = manage_news_media()
#     context['seo_title'] = news_media_topic + ' - Neo Events'
#     context['seo_description'] = news_media_contents
#     context['news_media_topic'] = news_media_topic
#     context['news_media_media_file'] = news_media_media_file
#     context['news_media_contents'] = news_media_contents
#     context['news_media_published_date'] = news_media_published_date
#     if news_media_list:
#         context['recommended_news_media'] = news_media_list[0:2]
#     return render(request, 'frontend/news-event-detail.html', context=context)


def services(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('services')
    services_dict = services_list()
    context['seo_title'] = seo_title
    context['seo_description'] = seo_description
    context['services_dict'] = services_dict
    return render(request, 'frontend/services.html', context=context)


def service_detail(request, category, id):
    context = basic_setup()
    service_category, service_name, service_image, service_content = service_details(
        category, id)
    context['seo_title'] = service_name + ' - Neo Services'
    context['seo_description'] = service_content
    context['service_category'] = service_category.replace('-', ' ').title()
    context['service_name'] = service_name
    context['service_image'] = service_image
    context['service_content'] = service_content
    return render(request, 'frontend/service_detail.html', context=context)


def career(request):
    seo_title, seo_description = manage_seo_content('career')
    noEntry, fieldNames, objectList = True, [], []
    objList = PostVacancies.objects.filter(status='current-opening').values()
    if objList:
        noEntry, fieldNames, objectList = return_object_list(objList)
    context = {
        "noEntry": noEntry,
        "objects": objectList,
        "fieldNames": fieldNames,
        "seo_title": seo_title,
        "seo_description": seo_description
    }
    return render(request, 'frontend/career.html', context=context)


def apply_career(request, id):
    jobApplied = False
    objectToAdd = PostVacancies.objects.filter(id=id).values()[0]
    if request.POST:
        objToSave = ResumeReceipt()
        for key in request.POST:
            if key != 'csrfmiddlewaretoken' and len(request.POST[key]) != 0:
                new_value = request.POST[key].replace(
                    '\r', '<br>').replace('\n', '<br>')
                setattr(objToSave, key, new_value)
        for key in request.FILES:
            file_instance = request.FILES[key]
            tempFileName = 'ResumeReceipt'+'_'+datetime.now().strftime("%m%d%y%H%M%S") + \
                '.'+str(request.FILES[key]).split('.')[-1]
            fs = FileSystemStorage()
            filename = fs.save(tempFileName, file_instance)
            uploaded_file_url = fs.url(filename)
            setattr(objToSave, key, uploaded_file_url)
        objToSave.save()
        jobApplied = True
    return render(request, 'frontend/apply-career.html', context={'jobApplied': jobApplied, "objectToAdd": objectToAdd, "id": id, })


def apply_job(request):
    jobApplied = False
    if request.POST:
        objToSave = ResumeReceipt()
        for key in request.POST:
            if key != 'csrfmiddlewaretoken' and len(request.POST[key]) != 0:
                new_value = request.POST[key].replace(
                    '\r', '<br>').replace('\n', '<br>')
                setattr(objToSave, key, new_value)
        for key in request.FILES:
            file_instance = request.FILES[key]
            tempFileName = 'ResumeReceipt'+'_'+datetime.now().strftime("%m%d%y%H%M%S") + \
                '.'+str(request.FILES[key]).split('.')[-1]
            fs = FileSystemStorage()
            filename = fs.save(tempFileName, file_instance)
            uploaded_file_url = fs.url(filename)
            setattr(objToSave, key, uploaded_file_url)
        objToSave.save()
        jobApplied = True
    return render(request, 'frontend/apply-job.html', context={'jobApplied': jobApplied})


def putSpace(input):
    words = re.findall('[A-Z][a-z]*', input)
    result = []
    for word in words:
        word = chr(ord(word[0]) + 32) + word[1:]
        result.append(word)
    return ' '.join(result).title()


def footer_contents(request, objectType):
    context = {}
    page_content = footer_content(objectType)
    page_title = putSpace(objectType)
    context['seo_title'] = page_title
    if len(page_content) > 160:
        context['seo_description'] = page_content[0:160]
    else:
        context['seo_description'] = page_content
    context['page_content'] = page_content
    context['page_title'] = page_title
    return render(request, 'frontend/footercontents.html', context=context)


def manage_team(request):
    context = {}
    team_list = manage_team_members()
    context['seo_title'] = 'Team Members'
    context['seo_description'] = 'Team Members working at ADFPAY Neo Bank.'
    context['team_list'] = team_list
    return render(request, 'frontend/manageteam.html', context=context)


def advisory_board(request):
    context = {}
    team_list = advisory_board_members()
    context['seo_title'] = 'Advisory Board'
    context['seo_description'] = 'Advisory Board Members working at ADFPAY Neo Bank.'
    context['team_list'] = team_list
    return render(request, 'frontend/advisoryboard.html', context=context)


def sendmessage(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        message = request.POST['message']
        contact = ContactUs(name=name, email=email,
                            phone_no=phone_no, message=message)
        contact.save()
        messages.success(request, 'Message Sent!')
    return redirect('frontend:contact')


def handler404(request, exception, status=404):
    return render(request, 'frontend/404.html')
