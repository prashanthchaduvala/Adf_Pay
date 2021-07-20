from django.shortcuts import render,redirect
from accounts.models import *
from django.contrib import messages #import messages
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from api.models import *
import re



def becomemember(request):
    return render(request,
                  template_name='frontend/sign-up.html')


def register(request):
    if request.method == 'POST':
        file = request.FILES
        
        full_name = request.POST.get("full_name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        password ='admin'
        residential_address = request.POST.get("residential_address")
        residential_address2 = request.POST.get("residential_address2")
        country = request.POST.get("country")
        state = request.POST.get("state")
        city = request.POST.get("city")
        zipcode = request.POST.get("zipcode")
        pan_card = request.POST.get("pancard")
        aadhar_card = request.POST.get("aadharcard")
        upload_photo = file.get("photo")
        if re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', pan_card):
            pass
        else:
            messages.error(request, "INVALID PAN NO.")
            return render(request, 'frontend/sign-up.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, 'frontend/sign-up.html')# pending
        else:
            user = User.objects.create_user(username=email,
                                          email=email,password=password)
            # user=User.objects.create_user(username=email,first_name=firstname,last_name=lastname,
            #                               email=email,password=password1)
            BecomeMember.objects.create(become_user=user,full_name=full_name, mobile=mobile, email=email, password=password,
                                            residential_address=residential_address,
                                            residential_address2=residential_address2,
                                            country=country, state=state, city=city, zipcode=zipcode, pancard=pan_card,
                                            aadharcard=aadhar_card,
                                            photo=upload_photo,status='pending',is_member=True)
            user = authenticate(username=email, password=password)
        # auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        if user:
            messages.success(request, "Registered successfully")
            return render(request, 'frontend/sign-in.html')
            # return render(request, 'login.html')

        else:
            print("gggggggggggggggggggg")
            messages.error(request, "Registration failed")

            return render(request, 'frontend/sign-up.html')

                # return redirect(step1)
    else:
        print("gggggggggggggg")
        return render(request, 'frontend/sign-up.html')

def sucess(request):

    return render(request,'login.html')

def completed(request):
    return render(request,'cug/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successfull")

            return redirect('cugdashboard')
        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'login.html')
    else:
        return redirect('login')



# def savedata(request):
#     fullname = request.POST.get("fullname")
#     mobile = request.POST.get("mobile")
#     email = request.POST.get("email")
#     password = request.POST.get("password")
#     residential_address = request.POST.get("residential_address")
#     residential_address2 = request.POST.get("residential_address2")
#     residential_address3 = request.POST.get("residential_address3")
#     country = request.POST.get("country")
#     state = request.POST.get("state")
#     city = request.POST.get("city")
#     zipcode = request.POST.get("zipcode")
#     pan_card = request.POST.get("pancard")
#     aadhar_card = request.POST.get("aadharcard")
#     upload_photo = request.POST.get("photo")
#     data = BecomeMember(full_name=fullname,mobile=mobile,email=email,password=password,residential_address=residential_address,
#                         residential_address2=residential_address2,residential_address3=residential_address3,
#                         country=country,state=state,city=city,zipcode=zipcode,pancard=pan_card,aadharcard=aadhar_card,
#                         photo=upload_photo)
#     res = data.save()
#     # messages.success(request, "saved.")
#     return render(request,"frontend/sign-up.html",{"message":"registration has completed ,please login with your details!!"})


# def login(request):
#     email = request.POST.get('Email')
#     password = request.POST.get('Password')
#     try:
#         data = BecomeMember.objects.get(email=email,password=password)
#         return render(request,'frontend/index.html')
#     except:
#         return render(request,'frontend/login.html')

def addbank(request):
    return render(request,'cug/bankdetials.html')

from crugapp.forms import *
def addnew(request):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        # photo = file.get('photo')

        account_holder_name = form.get('account_holder_name')
        bank = form.get('bank')
        ifsc = form.get('ifsc_code')
        account_type = form.get('account_type')
        account_number=form.get('account_number')

        abt_obj = Bankdetails.objects.create(bank_user=request.user,account_holder_name=account_holder_name,account_number=account_number,
                                             bank_name=bank,ifsc_code=ifsc,account_type=account_type)
        return redirect('index')
    else:
        return render(request, 'crug_logs/index.html')

@login_required(login_url='/sign-in/')
def index(request):
    try:
        bank = Bankdetails.objects.filter(bank_user=request.user)
        # for d in bank:
        #     print(d.bank_user,request.user, 'gggggggggggggggggggggg')
        return render(request,"crug_logs/show.html",{'bank':bank})
    except :
        return redirect('errorshow')
    #     # bank = Bankdetails.objects.all()
    #     return render(request,"crug_logs/show.html",{'bank':bank})




def edit(request, id):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        photo = file.get('photo')
        print(file,'hhhhhhhhhhhhhh')

        account_holder_name = form.get('account_holder_name')
        bank = form.get('bank')
        ifsc = form.get('ifsc_code')
        account_type = form.get('account_type')
        account_number=form.get('account_number')
        obj = Bankdetails.objects.filter(id=id)
        print(obj,'hhhhhhhttttttttttttttttttttttttttttttttttttttttttttt')

        bank = Bankdetails.objects.filter(id=id).update(account_holder_name=account_holder_name,account_number=account_number,
                                             bank_name=bank,ifsc_code=ifsc,account_type=account_type,photo=photo)

        return render(request,'crug_logs/index.html',{'obj':obj})
    else:
        obj = Bankdetails.objects.filter(id=id)
        return render(request,'crug_logs/edit.html',{'obj':obj})
    # bank = Bankdetails.objects.get(id=id)
    # form = BankdetailsForm(request.POST, instance = bank)
    # if form.is_valid():
    #     form.save()
    #     return redirect("index")
    # return render(request, 'crug_logs/edit.html', {'bank': bank})
    # # bank = Bankdetails.objects.get(id=id)
    # return render(request,'crug_logs/edit.html', {'bank':bank})


# def edit_about_us(request, id):
#     if request.method == 'POST':
#         form = request.POST
#         account_holder_name = form.get('account_holder_name')
#         bank = form.get('bank')
#         ifsc = form.get('ifsc_code')
#         account_type = form.get('account_type')
#         account_number = form.get('account_number')
#         file = request.FILES
#         photo = file.get('photo')
#         # now = datetime.datetime.now().time()
#
#         # merge_file = str(file1) + str(now)
#
#         abt_obj = Bankdetails.objects.filter(Bank_id=id)
#         print(abt_obj, "abt_objjjjjjjjjjjjjjjjjj")
#         Bankdetails.objects.filter(abt_id=id).update(account_holder_name=account_holder_name,account_number=account_number,
#                                                  bank_name=bank, ifsc_code=ifsc, account_type=account_type, photo=photo)
#         return redirect('/index/')
#     else:
#         bank = Bankdetails.objects.filter(abt_id=id)
#
#         return render(request, 'edit.html', {'bank': bank})
#

# def update(request, id):
#     pass

    # if request.method == 'POST':
    #     form = request.POST
    #     file = request.FILES
    #     photo = file.get('photo')
    #
    #     account_holder_name = form.get('account_holder_name')
    #     bank = form.get('bank')
    #     ifsc = form.get('ifsc_code')
    #     account_type = form.get('account_type')
    #     account_number=form.get('account_number')
    #     obj = Bankdetails.objects.filter(id=id)
    #     print(obj,'hhhhhhhttttttttttttttttttttttttttttttttttttttttttttt')
    #
    #     bank = Bankdetails.objects.filter(id=id).update(account_holder_name=account_holder_name,account_number=account_number,
    #                                          bank_name=bank,ifsc_code=ifsc,account_type=account_type,photo=photo)
    #     return render(request,'crug_logs/index.html',{'obj':obj})
    # else:
    #     return render(request,'crug_logs/edit.html',{'obj':obj})
    # bank = Bankdetails.objects.get(id=id)
    # form = BankdetailsForm(request.POST, instance = bank)
    # if form.is_valid():
    #     form.save()
    #     return redirect("index")
    # return render(request, 'crug_logs/edit.html', {'bank': bank})


def destroy(request, id):
    bank = Bankdetails.objects.filter(id=id)
    bank.delete()
    return redirect("index")


# from api.models import *

# def add_about_us(request, *args, **kwargs):
#     if request.method == 'POST':
#         form = request.POST
#         file = request.FILES
#         # file1 = file.get('icon')
#
#         heading = form.get('heading')
#         content = form.get('content')
#         vision = form.get('vision')
#         mission = form.get('mission')
#
#         abt_obj = Bankdetails.objects.create(heading=heading, vision=vision,
#                                          content=content, mission=mission)
#
#         context = {
#             'data': abt_obj,
#         }
#         return redirect('/admin_master/what_make_us/')
#     else:
#         return render(request, 'add_about_us.html')


#
# # Change action views.
# @csrf_exempt
# def change_action(request, objectId, state):
#     # print(state,"==============state++++++++++++++++")
#     obj = AboutUs.objects.get(abt_id=objectId)
#     if obj.action == "True":
#         print("something")
#         obj.action = False
#         obj.save()
#     if obj.action == "False":
#         print("something")
#         obj.action = True
#         obj.save()
#     print(obj.action)
#     return HttpResponse('Action Changed!')
#
#
# # About us Edit Views.
# def edit_about_us(request, id):
#     if request.method == 'POST':
#         form = request.POST
#         heading = form.get('heading')
#         content = form.get('content')
#         vision = form.get('vision')
#         mission = form.get('mission')
#         file = request.FILES
#         file1 = file.get('icon')
#         now = datetime.datetime.now().time()
#
#         merge_file = str(file1) + str(now)
#
#         abt_obj = AboutUs.objects.filter(abt_id=id)
#         print(abt_obj, "abt_objjjjjjjjjjjjjjjjjj")
#         AboutUs.objects.filter(abt_id=id).update(heading=heading, content=content, vision=vision, mission=mission)
#         return redirect('/admin_master/what_make_us/')
#     else:
#         abt_obj = AboutUs.objects.filter(abt_id=id)
#
#         return render(request, 'edit_about_us.html', {'abt_obj': abt_obj})
#
#
# # what_make_us.
# def what_make_us(request):
#     obj = AboutUs.objects.all()
#     for o in obj:
#         print(o.action)
#
#     # storage = messages.get_messages(request)
#     # print(storage,"-------------stroage------------")
#     #
#     # storage.used = True
#
#     return render(request, 'what_make_us.html', {'obj': obj})
#
#
# # Delete about us.
# def delete_abt_us(request, id):
#     abt_obj = AboutUs.objects.filter(abt_id=id).delete()
#     messages.warning(request, 'Record Deleted!!')
#     return redirect('/admin_master/what_make_us/')
@login_required(login_url='/frontend/sign-in/')
def view_registration(request):
    context ={}

    data = BecomeMember.objects.get(become_user=request.user)
    context = {
        'data': data,
    }
    return render(request,'viewregister.html',context=context)
    # return render(request, 'viewregister.html',{'data'/: data})
    # return render(request,'viewregister.html')


def edit_register(request, id):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        photo = file.get('photo')
        print(file,'hhhhhhhhhhhhhh')

        full_name = form.get('full_name')
        mobile = form.get('mobile')
        email = form.get('email')
        password = form.get('password')
        residential_address=form.get('residential_address')
        residential_address2 = form.get('residential_address2')
        country = form.get('country')
        state = form.get('state')
        city = form.get('city')
        zipcode = form.get('zipcode')
        obj = BecomeMember.objects.filter(id=id)

        user_profile = BecomeMember.objects.filter(id=id).update(city=city,photo=photo,full_name=full_name,mobile=mobile,email=email,password=password,
                                                         residential_address=residential_address,residential_address2=residential_address2,
                                                         country=country,state=state,zipcode=zipcode)
        print(user_profile,'uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')
        return redirect('viewregistration')
    else:
        obj = BecomeMember.objects.filter(id=id)
        return render(request,'crug_logs/editviewregister.html',{'obj':obj})


def destroy_register(request, id):
    data = BecomeMember.objects.filter(id=id)
    data.delete()
    return redirect('viewregistration')


# Suggetions
@login_required(login_url='/sign-in/')
def suggetions(request):
     # data=Feedback.objects.all()
    data = Feedback.objects.filter(feedback_user=request.user)
    return render(request, "suggentions/showsuggestions.html", {'data': data})

def addsuggetion(request):
    return render(request,'suggentions/suggetion.html')

def addsuggetions(request):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        # country = form.get('country')
        # state = form.get('state')
        profile_type = form.get('profile_type')
        name = form.get('name')
        email=form.get('email')
        phone_no = form.get('phone')
        date = form.get('date')
        feedback = form.get('feedback')
        status = form.get('status')

        abt_obj = Feedback.objects.create(feedback_user=request.user,date=date,profile_type=profile_type,name=name,email=email,phone_no=phone_no,
                                          feedback=feedback,company_response=status)
        return redirect('suggetions')
    else:
        return redirect('addsuggetion')




# Feedback
def addfeedback(request):
    return render(request,'feedback/feedback.html')

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
@login_required(login_url='/sign-in/')
def feedback(request):
    # data = Feedback.objects.all()
     res = requests.get('http://127.0.0.1:8000/api/v1/feedback/')
     json_data = res.json()
     for item in json_data:
        print(item,'pppppppppppppasssssworddddd')
     return render(request,"feedback/showfeedback.html",{'json_data':item})
    
    #  try:
    #     # data = Feedback.objects.filter(feedback_user=request.user)
         
    #  except:
    #      return redirect('errorfeedback')

    

# def feedback(request):
#     contact_list = Feedback.objects.all()
#     paginator = Paginator(contact_list, 25) # Show 25 contacts per page
#
#     page = request.GET.get('page')
#     try:
#         contacts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         contacts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         data = paginator.page(paginator.num_pages)
#
#     return render(request,"feedback/showfeedback.html", {"data": data})



def addfeedbacks(request):

    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        # country = form.get('country')
        # state = form.get('state')
        # region = form.get('region')
        name = form.get('name')
        email=form.get('email')
        phone_no = form.get('phone')
        # date = form.get('date')
        feedback = form.get('feedback')
        status = form.get('status')

        abt_obj = Feedback.objects.create(feedback_user=request.user,name=name,email=email,phone_no=phone_no,
                                          feedback=feedback,company_response=status)
        return redirect('feedback')
    else:
        return redirect('addfeedback')


def edit_feedback(request, id):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        country = form.get('country')
        state = form.get('state')
        region = form.get('region')
        name = form.get('name')
        email=form.get('email')
        phone_no = form.get('phone')
        date = form.get('date')
        feedback = form.get('feedback')
        status = form.get('status')

        obj = Feedback.objects.filter(id=id)
        feedback = Feedback.objects.filter(id=id).update(country=country,state=state,region=region,name=name,email=email,phone_no=phone_no,
                                          date=date,feedback=feedback,company_response=status)
        return redirect('feedback')
    else:
        obj = Feedback.objects.filter(id=id)
        return render(request,'feedback/editfeedback.html',{'obj':obj})


def destroy_feedback(request, id):
    data = Feedback.objects.filter(id=id)
    data.delete()
    return redirect('feedback')

# Downloads
@login_required(login_url='/sign-in/')
def download(request):
    res = requests.get('http://127.0.0.1:8000/api/v1/totaldownloadsandroid')
    json_data = res.json()
    for item in json_data:
        print(item,'pppppppppppppasssssworddddd')
    # data = TotalDownloadsAndroid.objects.filter(android_user=request.user)
    return render(request,"downloads/showdownloads.html",{'data':item})


def adddownload(request):
    return render(request,'downloads/adddownloads.html')


def adddownloads(request):

    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        # country = form.get('country')
        state = form.get('state')
        region = form.get('region')
        downloadcount = form.get('downloadcount')
        last_download=form.get('last_download')

        abt_obj = TotalDownloadsAndroid.objects.create(android_user=request.user,state=state,region=region,
                                          last_downloaded_on=last_download)
        return redirect('download')
    else:
        return redirect('adddownloads')


def edit_download(request,id):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        # country = form.get('country')
        state = form.get('state')
        region = form.get('region')
        downloadcount = form.get('downloadcount')
        last_download = form.get('last_download')

        obj = TotalDownloadsAndroid.objects.filter(id=id)
        feedback = TotalDownloadsAndroid.objects.filter(id=id).update(state=state,region=region,
                                          last_downloaded_on=last_download)
        return redirect('download')
    else:
        obj = TotalDownloadsAndroid.objects.filter(id=id)
        return render(request,'downloads/editdownloads.html',{'obj':obj})


def destroy_download(request,id):
    data = TotalDownloadsAndroid.objects.filter(id=id)
    data.delete()
    return redirect('download')


# Online User
@login_required(login_url='/sign-in/')
def onlineuser(request):
    data = OnlineUsersAndroid.objects.filter(online_user=request.user)
    return render(request,"onlineuser/showonline.html",{"data":data})


def addusers(request):
    return render(request, 'onlineuser/addonlineuser.html')


def addonlineuser(request):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        profile_type = form.get('profile_type')
        # state = form.get('state')
        # region = form.get('region')
        name = form.get('name')
        email = form.get('email')
        phone = form.get('phone')
        date = form.get('date')
        # usercount = form.get('usercount')

        abt_obj = OnlineUsersAndroid.objects.create(online_user=request.user,profile_type=profile_type,name=name,email=email,
                                                       phone_no=phone,last_updated=date)
        return redirect('onlineuser')
    else:
        return redirect('adduser')


def edit_onlineuser(request,id):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        profile_type = form.get('profile_type')
        # country = form.get('country')
        # state = form.get('state')
        # region = form.get('region')
        name = form.get('name')
        email = form.get('email')
        phone = form.get('phone')
        date = form.get('date')
        usercount = form.get('usercount')

        obj = OnlineUsersAndroid.objects.filter(id=id)
        feedback = OnlineUsersAndroid.objects.filter(id=id).update(profile_type=profile_type,name=name,email=email,
                                                       phone_no=phone,last_updated=date,)
        return redirect('onlineuser')
    else:
        obj = OnlineUsersAndroid.objects.filter(id=id)
        return render(request, 'onlineuser/editonlineuser.html', {'obj': obj})


def destroy_onlineuser(request,id):
    data = OnlineUsersAndroid.objects.filter(id=id)
    data.delete()
    return redirect('onlineuser')

import requests

@login_required(login_url='/sign-in/')
def reviews(request):
    res = requests.get('http://127.0.0.1:8000/api/v1/reviews/')
    json_data = res.json()

    for item in json_data:
        print(item,'pppppppppppppasssssworddddd')
        

    return render(request, "reviews/showreviews.html", {'json_data': item})


def addreview(request):
    return render(request, 'reviews/addreviews.html')


def addreviews(request):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        name = form.get('name')
        mobile = form.get('mobile')
        email = form.get('email')
        date = form.get('date')

        profile_type = form.get('profile_type')
        comment = form.get('comment')
        management = form.get('management')
        feedback_content = form.get('feedback_content')

        user_profile = Reviews.objects.create(reviews_user=request.user,name=name,date=date,phone_no=mobile, email=email,
                                                            profile_type=profile_type,
                                                            review_comment=comment, company_response=management,
                                              feedback_content=feedback_content)
        return redirect('reviews')

    return redirect('addreviews')


def edit_review(request,id):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES
        name = form.get('name')
        mobile = form.get('mobile')
        email = form.get('email')
        date = form.get('date')

        profile_type = form.get('profile_type')
        comment = form.get('comment')
        management = form.get('management')
        feedback_content = form.get('feedback_content')



        obj = Reviews.objects.filter(id=id)
        reviews = Reviews.objects.filter(id=id).update(name=name,date=date,phone_no=mobile, email=email,
                                                            profile_type=profile_type,
                                                            review_comment=comment, company_response=management,
                                              feedback_content=feedback_content)
        return redirect('reviews')
    else:
        obj = Reviews.objects.filter(id=id)
        return render(request,'reviews/editreviews.html',{'obj':obj})


def destroy_review(request,id):
    data = Reviews.objects.filter(id=id)
    data.delete()
    return redirect('reviews')

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db.models import Count

def logout_view(request):
    # logout(request)
    auth_logout(request)
    # del request.session['fullname']
    return render(request,'frontend/sign-in.html')

def cugdashboard(request):
    data = Reviews.objects.all().count()
    data_count = TotalDownloadsAndroid.objects.all().count()
    user_count = BecomeMember.objects.all().count()
    online_count = OnlineUsersAndroid.objects.all().count()
    print(user_count)
    responed_count=Reviews.objects.values('review_comment').annotate(dcount=Count('review_comment')).count()
    return render(request,'cugdashboard.html',context={'data':data,'data_count':data_count,'user_count':user_count,
                                                       'responed_count':responed_count,
                                                       'online_count':online_count})


#v {Groupname1:(Description1, Description2, Description3), GroupName2:(Description5. Description6, Description7)}

def backindex(request):
    return render(request,'backindex.html')


# def userimage(request):
#     data = BecomeMember.objects.all()
#     return render(request,'header.html',{'data':data})
from django.views.generic import ListView

# from django.shortcuts import render
# from django.core.paginator import Paginator

# # Create your views here.
#
# # #
# def feedback(request):
#     data = Feedback.objects.all()  # fetching all post objects from database
#     p = Paginator(data, 5)  # creating a paginator object
#     # getting the desired page number from url
#     page_number = request.GET.get('page')
#     try:
#         page_obj = p.get_page(page_number)  # returns the desired page object
#     except PageNotAnInteger:
#         # if page_number is not an integer then assign the first page
#         page_obj = p.page(1)
#     except EmptyPage:
#         # if page is empty then return last page
#         page_obj = p.page(p.num_pages)
#     data = {'page_obj': page_obj}
#     # sending the page object to index.html
#     return render(request, 'feedback/showfeedback.html', {"data":data})


# Change action views.
# @csrf_exempt
# def change_action(request, objectId,state):
#      print(state,"==============state++++++++++++++++")
#      obj = AboutUs.objects.get(abt_id=objectId)
#      obj.action=state
#      obj.save()
#
#      return HttpResponse('Action Changed!')

def viewserrorshow(request):
    return render(request,"crug_logs/show2.html")


def errorfeedback(request):
    return render(request,'feedback/showfeedback2.html')

from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def change_action(request, objectType, objectId):
     modelClass = globals()[objectType]
     model = Feedback.objects.get(id=objectId)
     action = request.GET['action']
     model.action = action
     model.save()
     return HttpResponse('Action Changed!')


@csrf_exempt
def change_user(request, objectType, objectId):
     modelClass = globals()[objectType]
     model = BecomeMember.objects.get(id=objectId)
     action = request.GET['action']
     model.action = action
     model.save()
     return HttpResponse('Action Changed!')


@csrf_exempt
def change_bank(request, objectType, objectId):
     modelClass = globals()[objectType]
     model = Bankdetails.objects.get(id=objectId)
     action = request.GET['action']
     model.action = action
     model.save()
     return HttpResponse('Action Changed!')

# Reviews
@csrf_exempt
def change_review(request, objectType, objectId):
     modelClass = globals()[objectType]
     model = Reviews.objects.get(id=objectId)
     action = request.GET['action']
     model.action = action
     model.save()
     return HttpResponse('Action Changed!')

# TotalDownloadsAndroid
@csrf_exempt
def change_download(request, objectType, objectId):
     modelClass = globals()[objectType]
     model = TotalDownloadsAndroid.objects.get(id=objectId)
     action = request.GET['action']
     model.action = action
     model.save()
     return HttpResponse('Action Changed!')

# OnlineUsersAndroid
@csrf_exempt
def change_online(request, objectType, objectId):
     modelClass = globals()[objectType]
     model = OnlineUsersAndroid.objects.get(id=objectId)
     action = request.GET['action']
     model.action = action
     model.save()
     return HttpResponse('Action Changed!')


def pendingdownloads(request):
    return render(request,'downloads/pendingdownload.html')


def loginfail(request):
    return render(request,'loginfail.html')


def forgotpass(request):
    return render(request,'forgotpass/forgotpass.html')


def getemail(request):
    email=request.POST.get('email')
    try:
        user = User.objects.get(username=email)
        print(user)
        return render(request,'forgotpass/getemail.html',{'user':user})
    except:
        # messages.error('plese provide correct email id')
        return render(request, 'forgotpass/forgotpass.html')


def sucesspass(request,id):
    if request.method != 'POST':
        form = request.POST
        file = request.FILES
        password = form.get('password')
        print(password)
        obj = User.objects.filter(id=id)
        User.objects.filter(id=id).update(password=password)
        return render('loginfail')
    else:
        obj = User.objects.filter(id=id)
        return redirect('redopass')


def redopass(request):
    return render(request,'forgotpass/redopass.html')

from django.contrib.auth.forms import PasswordResetForm
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "forgotpass/password_reset_email.html"
					c = {
						"email": user.email,
						'domain': '127.0.0.1:8000',
						'site_name': 'Website',
						"uid": urlsafe_base64_encode(force_bytes(user.pk)),
						'token': default_token_generator.make_token(user),
						'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
					except BadHeaderError:

						return HttpResponse('Invalid header found.')

					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect("/")
			messages.error(request, 'An invalid email has been entered.')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="forgotpass/password_reset.html",
				  context={"password_reset_form": password_reset_form})

