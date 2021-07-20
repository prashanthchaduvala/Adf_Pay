from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.mail import BadHeaderError, send_mail
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from uuid import uuid4
from json import dumps,loads
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import *
from accounts.models import UserProfilesAndroid, UserProfilesIOS, InternalUsers
from django.conf import settings

# Create your views here.

# User LogOut
@login_required
def user_logout(request):
    print('ddsds')
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

@login_required
def user_logout3(request):
    print('ddsds')
    logout(request)
    return HttpResponseRedirect(reverse('frontendindex'))

# @login_required

# Internal User Registeration
@login_required
def create_internal_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_no = request.POST.get("phone_no")
        designation = request.POST.get("designation")
        password = request.POST.get("password")
        function_names = request.POST.getlist("function_names")
        permission_types = request.POST.getlist("permission_types")
        action = 'Active'
        username = email.split('@')[0]

        try:
            if User.objects.get(email=email) or User.objects.get(username=username):
                messages.warning(request, 'Email Id already exists!')
                return render(request, "accounts/RegisterForm.html", context = {'operation':'create'})
        except Exception as e:
            print("Email Id doesn't exists!")
        user = User.objects.create_user(username=username, email=email, password=password, is_staff=True)
        users = InternalUsers(user_id=user.id, name=name, email=email, password=password, phone_no=phone_no, designation=designation, function_names=function_names, permission_types=permission_types, action=action)
        users.save()
        from_email = settings.EMAIL_HOST_USER
        subject = 'Account Created, Get Your Account Details Here! - Neobank'
        html_message = render_to_string('accounts/account_created.html', context={'name' : name, 'username' : username, 'email' : email, 'password' : password})
        plain_message = strip_tags(html_message)
        try:
            send_mail(subject=subject, message=plain_message, from_email=from_email, recipient_list=[email], html_message=html_message)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        messages.success(request, 'Account Created Successfully! Check your email for the password details.')
        return redirect('show_object_list', objectType='InternalUsers')
    return render(request, "accounts/RegisterForm.html", context = {'operation':'create'})

@login_required
def update_internal_user(request, id):
    objectToUpdate = InternalUsers.objects.filter(id=id).values()[0]
    function_names_list = eval(objectToUpdate['function_names'])
    permission_types_list = eval(objectToUpdate['permission_types'])
    if request.method == "POST":
        objToUpdate = InternalUsers.objects.get(id=id)
        user = User.objects.get(id = objToUpdate.user_id)
        for key in request.POST:
            if len(request.POST[key]) != 0 and key != 'csrfmiddlewaretoken':
                if key == 'function_names' or key == 'permission_types':
                    setattr(objToUpdate,key,request.POST.getlist(key))
                elif key == 'email':
                    email = request.POST[key]
                    username = email.split('@')[0]
                    setattr(objToUpdate,key,request.POST[key])
                    user.email = email
                    user.username = username
                    user.save()
                elif key == 'password':
                    setattr(objToUpdate,key,request.POST[key])
                    user.password = request.POST['password']
                    user.set_password(user.password)
                    user.save()
                else:
                    setattr(objToUpdate,key,request.POST[key])
        objToUpdate.save()
        messages.success(request, 'Account Updated Successfully!')
        return redirect('show_object_list', objectType='InternalUsers')
    return render(request, "accounts/RegisterForm.html", context = {'id' : id, 'objects' : objectToUpdate, 'function_names_list':function_names_list, 'permission_types_list':permission_types_list})

# Login Users
def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('admindashboard'))
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user_object = User.objects.get(email=email)
        username = user_object.username
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return HttpResponseRedirect(reverse('admindashboard'))
        elif user is not None and user.is_staff is not True:
            messages.warning(request, 'User exists but have no admin access!')
            return render(request, 'accounts/login.html', context = {})
        else:
            messages.error(request, 'Invalid Login Credentials!')
            return render(request, 'accounts/login.html', context = {})
    return render(request, 'accounts/login.html', context = {})


def user_logout1(request):
    print('ddsds')
    logout(request)
    return HttpResponseRedirect(reverse('user_login1'))

def user_login1(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('neoadmin'))
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user_object = User.objects.get(email=email)
        username = user_object.username
        user = authenticate(request,  username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return HttpResponseRedirect(reverse('neoadmin'))
        elif user is not None and user.is_staff is not True:
            messages.warning(request, 'User exists but have no admin access!')
            return render(request, 'accounts/cms_login.html', context = {})
        else:
            messages.error(request, 'Invalid Login Credentials!')
            return render(request, 'accounts/cms_login.html', context = {})
    return render(request, 'accounts/cms_login.html', context = {})


def forgot_password(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard'))
    if request.POST:
        email = request.POST['email']
        from_email = settings.EMAIL_HOST_USER
        subject = 'Reset Your Password - Neobank'
        key = uuid4()
        users = InternalUsers.objects.get(email=email)
        users.password_revovery_key = key
        users.save()
        recoverpasswordlink = request.get_host() + "/accounts/recoverpassword?email=" + email + "&recoverykey=" + str(users.password_revovery_key)
        html_message = render_to_string('accounts/forgot_pwd_mail.html', context={'recoverpasswordlink': recoverpasswordlink})
        plain_message = strip_tags(html_message)
        try:
            if User.objects.get(email = email):
                try:
                    send_mail(subject=subject, message=plain_message, from_email=from_email, recipient_list=[email], html_message=html_message)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                messages.success(request, 'Password recovery link sent to your email address.')
                return render(request, 'accounts/forgot-password.html', context = {})
        except Exception as e:
            raise e
            messages.warning(request, 'Email Id does not exists.')
            return render(request, 'accounts/forgot-password.html', context = {})
    return render(request, 'accounts/forgot-password.html', context = {})

def recover_password(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard'))
    if 'recoverykey' in request.GET:
        request.session['neoadmin_forgot_email'] = request.GET['email']
        request.session['neoadmin_recovery_key'] = request.GET['recoverykey']
        return render(request, 'accounts/recover-password.html', context = {})
    elif 'password' in request.POST:
        try:
            user = User.objects.get(email = request.session['neoadmin_forgot_email'])
            users = InternalUsers.objects.get(user_id = user.id, email=request.session['neoadmin_forgot_email'], password_revovery_key=request.session['neoadmin_recovery_key'])
        except Exception as e:
            messages.error(request, 'Invalid recovery key!')
            return render(request, 'accounts/recover-password.html', context = {})
        if request.POST['password'] == request.POST['cpassword']:
            user.password = request.POST['password']
            user.set_password(user.password)
            users.password_revovery_key = ''
            user.save()
            users.save()
            messages.success(request, 'Password reset successfully!')
            return HttpResponseRedirect(reverse('user_login'))
        else:
            messages.error(request, 'Password did not match!')
            return render(request, 'accounts/recover-password.html', context = {})
    else:
        return HttpResponseRedirect(reverse('forgot_password'))

@csrf_exempt
def create_user_profile_android(request):
    if request.method=='POST':
        user_profile_object = loads(request.body)
        name = user_profile_object['name']
        email = user_profile_object['email']
        username = user_profile_object['username']
        password = user_profile_object['password']
        phone_no = user_profile_object['phone_no']
        country = user_profile_object['country']
        state = user_profile_object['state']
        region = user_profile_object['region']
        profile_type = user_profile_object['profile_type']
        action = 'Active'
        try:
            if User.objects.get(email=email):
                return JsonResponse('Email ID already exists!')
        except Exception as e:
            print("Email Id doesn't exists!")
        user = User.objects.create_user(username=username, email=email, password=password)
        users = UserProfilesAndroid(user_id=user.id, name=name, email=email, phone_no=phone_no, country=country, state=state, region=region, profile_type=profile_type, action=action)
        users.save()
        return JsonResponse('User Profile Created!')

@csrf_exempt
def update_user_profile_android(request, id):
    if request.method=='POST':
        user_profile_object = loads(request.body)
        name = user_profile_object['name']
        email = user_profile_object['email']
        username = user_profile_object['username']
        password = user_profile_object['password']
        phone_no = user_profile_object['phone_no']
        country = user_profile_object['country']
        state = user_profile_object['state']
        region = user_profile_object['region']
        profile_type = user_profile_object['profile_type']
        user = User.objects.get(id = id)
        user.username = username
        user.password = password
        user.set_password(user.password)
        user.email = email
        user.save()
        users = UserProfilesAndroid.objects.get(user_id=user.id)
        users.name = name
        users.email = email
        users.phone_no = phone_no
        users.country = country
        users.state = state
        users.region = region
        users.profile_type = profile_type
        users.save()
        return JsonResponse('User Profile Updated!')

def get_user_profile_android(request):
    user_profile_object = UserProfilesAndroid.objects.all().values()

def create_user_profile_ios(request):
    if request.method=='POST':
        user_profile_object = loads(request.body)
        name = user_profile_object['name']
        email = user_profile_object['email']
        username = user_profile_object['email'].split('@')[0]
        password = user_profile_object['password']
        phone_no = user_profile_object['phone_no']
        country = user_profile_object['country']
        state = user_profile_object['state']
        region = user_profile_object['region']
        profile_type = user_profile_object['profile_type']
        action = 'Active'
        try:
            if User.objects.get(email=email):
                return JsonResponse('Email ID already exists!')
        except Exception as e:
            print("Email Id doesn't exists!")
        user = User.objects.create_user(username=username, email=email, password=password)
        users = UserProfilesIOS(user_id=user.id, name=name, email=email, phone_no=phone_no, country=country, state=state, region=region, profile_type=profile_type, action=action)
        users.save()

def get_user_profile_ios(request):
    user_profile_object = UserProfilesIOS.objects.all().values()
