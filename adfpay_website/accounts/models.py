from django.db import models
from django.contrib.auth.models import User
import re
from django.conf import settings
# from django.contrib.auth import get_user_model
# from api.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class InternalUsers(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='internal_users')
    name = models.CharField(default="", max_length=200)
    email = models.EmailField(default="", max_length=200, unique=True)
    password = models.CharField(default="", max_length=300)
    phone_no = models.CharField(default="", max_length=200, unique=True)
    designation = models.CharField(default="", max_length=200)
    function_names = models.CharField(default="", max_length=2000)
    permission_types = models.CharField(default="", max_length=200)
    password_revovery_key = models.CharField(default="", max_length=200)
    action = models.CharField(default="", max_length=200)

class BecomeMember(models.Model):
    become_user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='become_users',null=True,blank=True)
    full_name = models.CharField(max_length=50,null=True,blank=True)
    mobile = PhoneNumberField(default='', unique=True)
    email = models.EmailField(max_length=150,null=True,blank=True)
    password = models.CharField(max_length=8,null=True,blank=True,default='admin')
    residential_address = models.CharField(max_length=100,null=True,blank=True)
    residential_address2 = models.CharField(max_length=100,null=True,blank=True)
    residential_address3 = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=70,null=True,blank=True)
    zipcode = models.IntegerField(default='')
    pancard = models.CharField(max_length=10,null=True,blank=True)
    aadharcard = models.IntegerField(default='')
    photo = models.FileField(upload_to='become_member/',null=True,blank=True)
    action = models.BooleanField(default=False,null=True,blank=True)
    status = models.CharField(max_length=10)
    userreg_date = models.DateTimeField(auto_now_add=True)
    is_member=models.BooleanField(default='True')



    class Meta:
        verbose_name_plural = 'Become_member'

    def __str__(self):
        return self.full_name


class UserProfilesAndroid(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='user_profiles_android')
    email = models.EmailField(default="", max_length=200, unique=True)
    country = models.CharField(default="", max_length=200)
    state = models.CharField(default="", max_length=200)
    region = models.CharField(default="", max_length=200)
    name = models.CharField(default="", max_length=200)
    phone_no = models.CharField(default="", max_length=200, unique=True)
    profile_type = models.CharField(default="", max_length=200)
    last_updated = models.DateTimeField(auto_now=True)
    action = models.CharField(default="", max_length=200)

class UserProfilesIOS(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='user_profiles_ios')
    email = models.EmailField(default="", max_length=200, unique=True)
    country = models.CharField(default="", max_length=200)
    state = models.CharField(default="", max_length=200)
    region = models.CharField(default="", max_length=200)
    name = models.CharField(default="", max_length=200)
    phone_no = models.CharField(default="", max_length=200, unique=True)
    profile_type = models.CharField(default="", max_length=200)
    last_updated = models.DateTimeField(auto_now=True)
    action = models.CharField(default="", max_length=200)
