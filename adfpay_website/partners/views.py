from django.shortcuts import render,redirect
from partners.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from dashboard.models import *
from django.contrib.auth.models import User
# Create your views here
@login_required
def index(request):
    return render(request,"newpartner.html")


def usersave(request):
    if request.method == 'POST':
        name = request.POST.get("fullname")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        password='admin'
        residential_address = request.POST.get("adddress")
        residential_address2 = request.POST.get("address2")
        country = request.POST.get("country")
        state = request.POST.get("state")
        city = request.POST.get("city")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request,'frontend/sign-up.html')
        else:
            user = User.objects.create_user(username=email,
                                          email=email,password=password)
            data=Becomepartner.objects.create(become_user=user,username=name,mobile=mobile,email=email,password=password,residential_address=residential_address,
                                     locality=residential_address2,country=country,state=state,city=city,status='pending',is_partner=True)
            message = ('your registration was sucessfull ,we will get back you soon!!')
            return render(request,'userdata.html',{"message":message})
    else:
        return render(request,'frontend/becomepartner.html')



# @login_required(login_url='/frontend/become_partner/')
def download(request):
    # data = Download.objects.filter(download_user=request.user) # login user
    data = Download.objects.all() # all users
    return render(request,"partners/showpartner.html",{"data":data})


# @login_required(login_url='/')
def onlineuser(request):
    # data = OnlineUsersAndroid.objects.filter(online_user=request.user) # login user
    data = OnlineUsers.objects.all() # all users
    return render(request,"partners/showonlinepartner.html",{"data":data})


# @login_required(login_url='/frontend/become_partner/')
def aquasization(request):
    # data = DownloadApp.objects.filter(aquasization_user=request.user) # login user
    data = DownloadApp.objects.all()
    return render(request,"partners/showaquasization.html",{"data":data})


# @login_required(login_url='/frontend/become_partner/')
def userprofile(request):
    if request.user.is_authenticated:
        user = Becomepartner.objects.filter(become_user=request.user) # login user
    # user = Becomepartner.objects.all()
        print(user,'pppppppppppppppppppppppppppppp')
        return render(request,"partners/users.html",{"user":user})
    else:
        message = 'your not login please login with your details!!'
        return render(request, 'frontend/sign-in-download.html',{"message":message})


# logout User
def logoutpartner(request):
    auth_logout(request)
    # user = Becomepartner().force_logout()
    # user.is_active = False
    return render(request,'frontend/sign-in-download.html')

# Referall Partener Performance
def referallpartner(request):
    # data = ReferallPartner.objects.filter(referallpartner=request.user) # login user
    data = ReferallPartner.objects.all()
    return render(request,'partners/showrefer.html',{"data":data})


def commision(request):
    # data = Commission.objects.filter(referallpartner=request.user)  # login user
    data = Commission.objects.all()
    return render(request, 'partners/commisionshow.html', {"data": data})


def approvedrate(request):
    # data = Commission.objects.filter(referallpartner=request.user)  # login user
    data = ApproveRate.objects.all()
    return render(request, 'partners/approvedrate.html', {"data": data})

@login_required
def countheader(request):
    data =DownloadApp .objects.all().count()
    data_count = Download.objects.all().count()
    user_count = Becomepartner.objects.all().count()
    online_count = ReferallPartner.objects.all().count()
    return render(request,'partners/mainhead.html',context={'data':data,'data_count':data_count,'user_count':user_count,
                                                       'online_count':online_count})
#
# from django.contrib.auth import logout
# from django.utils.deprecation import MiddlewareMixin
# import datetime
# class MyUser(Becomepartner):
#     force_logout_date = models.DateTimeField(null=True, blank=True)
#
#     def force_logout(self):
#         self.force_logout_date = datetime.now()
#         self.save()
def log(request):
    return render(request, 'partners/loginusr.html')

def loginuser(request):
    email =request.POST.get("email")
    password = request.POST.get("password")
    if email =='admin@gmail.com' and  password == 'admin123':
        return redirect('downloadpartner')
    else:
        return redirect('/')


def partnerlogin(request):
    return render(request,'partners/partnerlogin.html')