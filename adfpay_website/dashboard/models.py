from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here         
# class User(AbstractUser):
#   country = models.CharField(max_length=20,null=True,blank=True)
#   state = models.CharField(max_length=20,null=True,blank=True)
#   region = models.CharField(max_length=20,null=True,blank=True)
#   name = models.CharField(max_length=100,null=False, blank=False, unique=True)
#   phonenumber = PhoneNumberField(blank=True)
#   profile_type = models.CharField(max_length=50,null=True,blank=False)
#   updated_at = models.DateTimeField(auto_now=True,null=True)
#   created_at = models.DateTimeField(auto_now_add=True,null=True)
#   action = models.BooleanField(default=False)


#   def __str__(self):
#       return self.username

#   class Meta:
#       db_table = "user"

class PermissionMenu(models.Model):
    INACTIVE = 0
    ACTIVE = 1
    STATUS = (
        (INACTIVE, ('Inactive')),
        (ACTIVE, ('Active')),
    )
    status = models.IntegerField(default=1, choices=STATUS)
    permission_menu = models.CharField(max_length=100)

    def __str__(self):  # __unicode__ on Python 2
        return self.permission_menu


class PermissionSubMenu(models.Model):
    INACTIVE = 0
    ACTIVE = 1
    STATUS = (
        (INACTIVE, ('Inactive')),
        (ACTIVE, ('Active')),
    )
    menu_id = models.ForeignKey(PermissionMenu, on_delete=models.CASCADE)
    status = models.IntegerField(default=1, choices=STATUS)
    permission_sub_menu = models.CharField(max_length=100)

    def __str__(self):  # __unicode__ on Python 2
        return self.permission_sub_menu



class Android(models.Model):
    ad_id= models.AutoField(primary_key=True)
    version = models.CharField(max_length=100,null=False, blank=False)
    release_date = models.DateField()
    images = models.FileField(upload_to='images/',blank=True,null=True)
    action = models.BooleanField(default=False)

    def __str__(self):
        return self.version

    class Meta:
        db_table = "android"

class Ios(models.Model):
    ad_id= models.AutoField(primary_key=True)
    version = models.CharField(max_length=100,null=False, blank=False)
    release_date = models.DateField()
    images = models.FileField(upload_to='images/',blank=True,null=True)
    action = models.BooleanField(default=False)

    def __str__(self):
        return self.version

    class Meta:
        db_table = "Ios"

class Download(models.Model):
    d_id=models.AutoField(primary_key=True)
    country=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    region=models.CharField(max_length=100,null=True,blank=True)
    counting = models.PositiveIntegerField(default=0)
    last_downloaded_on = models.DateField()

    def __str__(self):
        return self.country

    class Meta:
        db_table = "Download"

class DownloadApp(models.Model):
    d_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    phonenumber = PhoneNumberField(blank=True)
    email_id=models.EmailField(max_length=254,null=True,blank=True)
    request_date = models.DateTimeField(auto_now=True,null=True)
    download_date = models.DateTimeField(auto_now_add=True,null=True)
    action = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "DownloadApp"

class UserProfile(models.Model):
    d_id=models.AutoField(primary_key=True)
    country=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    region=models.CharField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    mobile_Number=PhoneNumberField(blank=True)
    email_id=models.EmailField(max_length=254,null=True,blank=True)
    profile_type=models.CharField(max_length=100,null=True,blank=True)
    last_updated= models.DateField()
    action = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "UserProfile"


class OnlineUser(models.Model):
    d_id=models.AutoField(primary_key=True)
    country=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    region=models.CharField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    mobile_Number=PhoneNumberField(blank=True)
    email_id=models.EmailField(max_length=254,null=True,blank=True)
    profile_type=models.CharField(max_length=100,null=True,blank=True)
    last_updated= models.DateField()
    action = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "OnlineUser"

class Restores(models.Model):
    d_id=models.AutoField(primary_key=True)
    country=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    region=models.CharField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    mobile_Number=PhoneNumberField(blank=True)
    email_id=models.EmailField(max_length=254,null=True,blank=True)
    profile_type=models.CharField(max_length=100,null=True,blank=True)
    last_updated= models.DateField()
    action = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Restores"

class Services(models.Model):
    country = models.CharField(default="", max_length=300,null=True)
    state = models.CharField(default="", max_length=300,null=True)
    region=models.CharField(default="", max_length=300,null=True)
    name = models.CharField(default="", max_length=300,null=True)
    mobile_no = models.IntegerField(default=-1,null=True)
    email_id = models.EmailField(null=True)
    profile_type=models.CharField(default="", max_length=300,null=True)
    service_type = models.CharField(default="", max_length=300,null=True)
    service_name = models.CharField(default="", max_length=300,null=True)
    service_charge=models.IntegerField(default=-1,null=True)
    date_of_utilization=models.DateField(null=True, blank=True)
    mode_of_receipt=models.CharField(default="", max_length=300,null=True)
    receipt_date=models.DateField(null=True, blank=True)
    outstanding_amount=models.IntegerField(default=-1 ,null=True)
    outstanding_since=models.DateField(null=True, blank=True)
    gst_rate=models.IntegerField(default=-1,null=True)
    gst_amount = models.IntegerField(default=-1,null=True)
    total_charges = models.IntegerField(default=-1,null=True)
    status = models.CharField(default="Active", max_length=10,null=True)
    action = models.CharField(default="-1", max_length=10,null=True)


class Subscription(models.Model):
    d_id=models.AutoField(primary_key=True)
    country=models.CharField(max_length=100,null=True,blank=True)
    profile_type=models.CharField(max_length=100,null=True,blank=True)
    currency=models.CharField(max_length=100,null=True,blank=True)
    amount=models.PositiveIntegerField()
    subscription_type=models.CharField(max_length=100,null=True,blank=True)
    collection_method=models.CharField(max_length=100,null=True,blank=True) 
    action = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Subscription"  



class OnlineSubscriber(models.Model):
    d_id=models.AutoField(primary_key=True)
    country=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    region=models.CharField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    mobile_Number=PhoneNumberField(blank=True)
    email_id=models.EmailField(max_length=254,null=True,blank=True)
    profile_type=models.CharField(max_length=100,null=True,blank=True)
    currency=models.CharField(max_length=100,null=True,blank=True)
    amount=models.PositiveIntegerField()
    subscription_type=models.CharField(max_length=100,null=True,blank=True)
    collection_method=models.CharField(max_length=100,null=True,blank=True)
    start_date= models.DateField()
    end_date= models.DateField() 
    action = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "OnlineSubscriber"                

from datetime import date, datetime
import calendar

# Create your models here.
class Discount(models.Model):
    country = models.CharField(default="", max_length=300)
    profile_type = models.CharField(default="", max_length=300)
    discount_type = models.CharField(default="", max_length=300)
    discount_name = models.CharField(default="", max_length=300)
    coupon_number = models.CharField(default="", max_length=300)
    amount = models.IntegerField(default=-1)
    coupon_series_from=models.CharField(default="", max_length=300)
    coupon_series_till=models.CharField(default="", max_length=300)
    issue_date=models.DateField(null=True)
    valid_till=models.DateField(null=True)
    status=models.CharField(default="Active", max_length=20)
    action = models.CharField(default="Active", max_length=10)
    ipadress=models.TextField(null=True)
    macadress=models.TextField(null=True)
    remark=models.TextField(null=True)
    mobileno=models.IntegerField(default=-1,)
    utilization_date=models.DateField(null=True)
    user_name=models.CharField(default="", max_length=50)
    email_id=models.EmailField(null=True)


#priyanka
class Mail(models.Model):
    country = models.CharField(default="", max_length=300,null=True)
    state= models.CharField(default="", max_length=300,null=True)
    city= models.CharField(default="", max_length=300,null=True)
    client= models.CharField(default="", max_length=300)
    mobile_no= models.IntegerField(default=-1,null=True)
    email_id=models.EmailField(null=True)
    service_name=models.CharField(default="", max_length=300,null=True)
    mail_date=models.DateField(null=True)
    mail_content=models.TextField(null=True)
    ticket_id=models.IntegerField(default=-1,null=True)
    date=models.DateField(null=True)
    allocated_to=models.CharField(default="Active", max_length=300,null=True)
    allocated_date=models.DateField(null=True)
    esclated_to=models.CharField(default="Active", max_length=300,null=True)
    esclated_date=models.DateField(null=True)
    solution_detail=models.TextField(null=True)
    solution_date=models.DateField(null=True)
    pending_since=models.DateField(null=True)
    expired_on=models.DateField(null=True)
    status=models.CharField(default="Active", max_length=20,null=True)
    action=models.CharField(default="Active", max_length=20,null=True)


class Ticket(models.Model):
    ticket_id = models.IntegerField(default=-1)
    country = models.CharField(default="", max_length=300)
    state= models.CharField(default="", max_length=300)
    city= models.CharField(default="", max_length=300)
    client= models.CharField(default="", max_length=300)
    mobile_no= models.IntegerField(default=-1)
    email_id=models.EmailField()
    service_name=models.CharField(default="", max_length=300)
    concern=models.CharField(default="", max_length=300)
    date=models.DateField()
    allocated_to = models.CharField(default="Active", max_length=300)
    allocated_date = models.DateField()
    response_date = models.DateField()
    response_details = models.CharField(default="", max_length=300)
    esclated_to = models.CharField(default="Active", max_length=300)
    esclated_date = models.DateField()
    expired_on=models.DateField(null=True)
    pending_since = models.DateField()
    status=models.CharField(default=" ", max_length=10)
    action=models.CharField(default="Active", max_length=10)




class ChatBot(models.Model):
    ticket_id = models.IntegerField(default=-1,)
    country = models.CharField(default="", max_length=300)
    state= models.CharField(default="", max_length=300)
    city= models.CharField(default="", max_length=300)
    client= models.CharField(default="", max_length=300)
    mobile_no= models.IntegerField(default=-1)
    email_id=models.EmailField(null=True)
    service_name=models.CharField(default="", max_length=300)
    concern=models.CharField(default="", max_length=300)
    request_date=models.DateField(null=True,blank=True)
    request_contents=models.TextField(default=" ", max_length=300)
    date=models.DateField(null=True,blank=True)
    allocated_to = models.CharField(default="Active", max_length=300)
    allocated_date = models.DateField(null=True,blank=True)
    response_date = models.DateField(null=True,blank=True)
    response_details = models.CharField(default="", max_length=300)
    esclated_to = models.CharField(default="Active", max_length=300)
    esclated_date = models.DateField(null=True,blank=True)
    expired_on=models.DateField(null=True,blank=True)
    pending_since = models.DateField(null=True,blank=True)
    solution_detail = models.TextField(default="", max_length=300)
    solution_date = models.DateField(null=True,blank=True)
    status=models.CharField(default=" ", max_length=10)
    action=models.CharField(default="Active", max_length=10)



class PhoneConversation(models.Model):
    ticket_id = models.IntegerField(default=-1, )
    country = models.CharField(default="", max_length=300)
    state= models.CharField(default="", max_length=300)
    city= models.CharField(default="", max_length=300)
    client= models.CharField(default="", max_length=300)
    mobile_no= models.IntegerField(default=-1)
    email_id=models.EmailField(null=True)
    service_name=models.CharField(default="", max_length=300)
    call_date=models.DateField(null=True, blank=True)
    call_contents=models.TextField(default="",max_length=300,null=True)
    concern=models.CharField(default="", max_length=300)
    request_date=models.DateField(null=True, blank=True)
    request_contents=models.TextField(default="",max_length=300)
    date=models.DateField(null=True, blank=True)
    allocated_to = models.CharField(default="Active", max_length=300)
    allocated_date = models.DateField(null=True, blank=True)
    response_date = models.DateField(null=True, blank=True)
    response_details = models.CharField(default="", max_length=300)
    esclated_to = models.CharField(default="Active", max_length=300)
    esclated_date = models.DateField(null=True, blank=True)
    expired_on=models.DateField(null=True, blank=True)
    pending_since = models.DateField(null=True, blank=True)
    solution_detail = models.TextField(default="",max_length=300)
    solution_date = models.DateField(null=True, blank=True)
    status=models.CharField(default=" ", max_length=10)
    action=models.CharField(default="Active", max_length=10)

class ReferAndEarn(models.Model):
    country = models.CharField(default="", max_length=300)
    profile_type=models.CharField(default="", max_length=300)
    incentive_type = models.CharField(default="", max_length=300)
    incentive_name = models.CharField(default="", max_length=300)
    amount=models.IntegerField(default=-1)
    name=models.CharField(default=-1, max_length=300)
    email_id=models.EmailField(null=True, blank=True)
    mobile_no= models.IntegerField(default=-1)
    mode_of_payment=models.CharField(default="", max_length=300,null=True)
    earned_on = models.DateField(null=True, blank=True)
    paid_on=models.DateField(null=True, blank=True)
    outstanding_since=models.DateField(null=True, blank=True)
    action=models.CharField(default="Active", max_length=10)




class CommuityMember(models.Model):
    country = models.CharField(default="", max_length=300)
    state = models.CharField(default="", max_length=300)
    city = models.CharField(default="", max_length=300)
    name = models.CharField(default="", max_length=300)
    mobile_no = models.IntegerField(default=-1)
    email_id = models.EmailField(null=True, blank=True)
    documents=models.FileField(null=True)
    date=models.DateField(null=True, blank=True)
    application_date=models.DateField(null=True, blank=True)
    allocated_to = models.CharField(default="Active", max_length=300)
    allocated_date = models.DateField(null=True, blank=True)
    approval_date=models.DateField(null=True, blank=True)
    active_since=models.IntegerField(default=-1)
    amount=models.IntegerField(default=-1)
    paid_on=models.DateField(null=True, blank=True)
    invoice_month_and_year=models.CharField(default="", max_length=300)
    invoice_number=models.IntegerField(default=-1)
    user_id=models.CharField(default="", max_length=300)
    password=models.CharField(default="", max_length=300)
    active_since=models.DateField(null=True, blank=True)
    users_added=models.CharField(default="", max_length=300)
    action = models.CharField(default="-1", max_length=10)
    status = models.CharField(max_length=10)


class TransactionHistory(models.Model):
    country= models.CharField(default="", max_length=50)
    state=models.CharField(default="", max_length=50)
    region= models.CharField(default="",max_length=50)
    profile_type= models.CharField(default="", max_length=50)
    name = models.CharField(default="", max_length=300, null=True)
    mobile_no = models.IntegerField(default=-1, null=True)
    email_id = models.EmailField(null=True)
    service_type = models.CharField(default="", max_length=50)
    service_name = models.CharField(default="", max_length=50)
    transaction_type = models.CharField(default="", max_length=50)
    initiation_date=models.DateField(null=True, blank=True)
    amount= models.IntegerField(default=-1, null=True)
    completed_on=models.DateField(null=True, blank=True)
    ip_address= models.CharField(default="", max_length=50)
    mac_address= models.CharField(default="", max_length=50)
    remark= models.CharField(default="", max_length=50)
    status= models.CharField(default="", max_length=50)
    action= models.CharField(default=-1, max_length=50)


class PartnerPayoutStructure(models.Model):
    country = models.CharField( max_length=50)
    state = models.CharField( max_length=50)
    city = models.CharField(max_length=50)
    name  = models.CharField( max_length=50)
    mobile =PhoneNumberField(blank=True)
    email = models.EmailField(max_length=150,null=True)
    active_since  =models.DateField(null=True,blank=True)
    user_range = models.CharField( max_length=50)
    payout_rate = models.CharField( max_length=50)
    currency = models.CharField(max_length=50)
    start_date = models.DateField(null=True,blank=True)
    valid_till_date = models.DateField(null=True,blank=True)
