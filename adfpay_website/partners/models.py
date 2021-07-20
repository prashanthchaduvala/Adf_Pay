from django.db import models
import uuid
from django.contrib.auth.models import User

class Becomepartner(models.Model):
    become_user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='become_partner')
    username= models.CharField(max_length=50)
    mobile = models.IntegerField(unique=True)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=8,null=True,blank=True,default='admin')
    residential_address = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=70)
    status = models.CharField(max_length=10)
    is_partner=models.BooleanField(default='True')


class Download(models.Model):
    download_user = models.ForeignKey(Becomepartner,on_delete=models.CASCADE,blank=True,null=True)
    country = models.CharField(default="", max_length=200)
    state = models.CharField(default="", max_length=200)
    city = models.CharField(default="", max_length=200)
    counting = models.PositiveIntegerField(default=0)
    last_downloaded_on = models.CharField(default="", max_length=200)

class OnlineUsers(models.Model):
    download_user = models.ForeignKey(Becomepartner,on_delete=models.CASCADE,blank=True,null=True)
    email = models.EmailField(default="", max_length=200, unique=True)
    state = models.CharField(default="", max_length=200)
    region = models.CharField(default="", max_length=200)
    name = models.CharField(default="", max_length=200)
    phone_no = models.CharField(default="", max_length=200, unique=True)
    profile_type = models.CharField(default="", max_length=200)
    last_updated = models.DateTimeField(auto_now=True,null=True,blank=True)
    action = models.CharField(default="Active", max_length=200)
    current_users_count = models.PositiveIntegerField(default=0)



class ReferallPartner(models.Model):
    refarall = models.ForeignKey(Becomepartner,on_delete=models.CASCADE)
    # location =models.CharField(max_length=80)
    profile_type = models.CharField(max_length=25)
    service = models.CharField(max_length=35)
    perform_name = models.CharField(max_length=45)
    dateofperformance = models.DateField()


class Commission(models.Model):
    commision = models.ForeignKey(Becomepartner,on_delete=models.CASCADE)
    service = models.CharField(max_length=35)
    volume = models.IntegerField()
    rate = models.IntegerField()

class ApproveRate(models.Model):
    approverate = models.ForeignKey(Becomepartner,on_delete=models.CASCADE)
    service = models.CharField(max_length=35)
    volume = models.IntegerField()
    rate = models.IntegerField()