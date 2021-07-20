from django.db import models
from django.core.files.storage import FileSystemStorage
# from .models import Post
from accounts.models import *
# Create your models here.

class CountryCode(models.Model):
    countrycode=models.CharField(default="", max_length=300,blank=True,null=True)
    mobile=models.CharField(default="", max_length=300,blank=True,null=True)


class ManageNewsMedia(models.Model):
    topic = models.CharField(default="", max_length=300,blank=True,null=True)
    content_type = models.CharField(default="", max_length=300,blank=True,null=True)
    content = models.TextField(default="",blank=True,null=True)
    content_display_type = models.CharField(default="", max_length=300,blank=True,null=True)
    media_file = models.FileField(upload_to='media/news_media',default="",blank=True,null=True)
    publisher_name= models.CharField(default="", max_length=300,blank=True,null=True)
    published_date = models.DateField(auto_now_add=True,blank=True,null=True)
    action = models.CharField(default="Active", max_length=10,blank=True,null=True)


class ManageSEOContent(models.Model):
    page_name = models.CharField(default="", max_length=300)
    title = models.CharField(default="", max_length=300)
    meta_description = models.CharField(default="", max_length=1000)
    action = models.CharField(default="Active", max_length=10)

class PostVacancies(models.Model):
    location = models.CharField(default="", max_length=300)
    department = models.CharField(default="", max_length=300)
    designation = models.CharField(default="", max_length=300)
    no_of_vacancies = models.PositiveIntegerField(default=0)
    experience = models.CharField(default="", max_length=300)
    qualification = models.CharField(default="", max_length=300)
    salary_range = models.CharField(default="", max_length=300)
    requirement_type = models.CharField(default="", max_length=300)
    valid_upto = models.DateField(default="")
    job_description = models.TextField(default="")
    status = models.CharField(default="", max_length=300)
    action = models.CharField(default="Active", max_length=300)

def get_resume_upload_path(instance, filename):
    return 'resumes/{0}/{1}'.format(instance.candidate_name, filename)

class ResumeReceipt(models.Model):
    candidate_name = models.CharField(default="", max_length=300)
    department = models.CharField(default="", max_length=300)
    designation = models.CharField(default="", max_length=300)
    location = models.CharField(default="", max_length=300)
    resume = models.FileField(upload_to=get_resume_upload_path, default="")
    action = models.CharField(default="Active", max_length=300)

class PublishBlogs(models.Model):
    publisher_name = models.CharField(default="", max_length=300)
    frontend_show = models.CharField(max_length = 20,blank=True,null=True)
    topic = models.CharField(default="", max_length=300)
    image = models.FileField(upload_to='blogs/%Y/%m/%d/', default="")
    content = models.TextField(default="")
    content_display_type = models.CharField(default="", max_length=300)
    published_date = models.DateField(auto_now_add=True)
    action = models.CharField(default="Active", max_length=300)

class ApproveComments(models.Model):
    blogid = models.PositiveIntegerField(default=0)
    publisher_name = models.CharField(default="", max_length=300)
    topic = models.CharField(default="", max_length=300)
    child = models.BooleanField(default=False)
    parent = models.IntegerField(default=-1)
    comment = models.CharField(default="", max_length=2000)
    commentator_name = models.CharField(default="", max_length=300)
    status = models.CharField(default="pending", max_length=300)
    action = models.CharField(default="Active", max_length=300)

class Partners(models.Model):
    logo = models.FileField(upload_to='partners', default="")
    name = models.CharField(default="", max_length=300)
    action = models.CharField(default="Active", max_length=300)

class Testimonials(models.Model):
    photo = models.FileField(upload_to='testimonials', default="")
    name = models.CharField(default="", max_length=300)
    profession = models.CharField(default="", max_length=300)
    comment = models.CharField(default="", max_length=1000)
    action = models.CharField(default="Active", max_length=300)

class MobileAppAndroid(models.Model):
    version_number = models.CharField(default="", max_length=300)
    release_date = models.DateField()
    upload = models.FileField(upload_to='mobileapp/android/%Y/%m/%d/', default="")

class MobileAppIOS(models.Model):
    version_number = models.CharField(default="", max_length=300)
    release_date = models.DateField()
    upload = models.FileField(upload_to='mobileapp/ios/%Y/%m/%d/', default="")

class TotalDownloadsAndroid(models.Model):
    android_user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    country = models.CharField(default="", max_length=200)
    state = models.CharField(default="", max_length=200)
    region = models.CharField(default="", max_length=200)
    counting = models.PositiveIntegerField(default=0)
    last_downloaded_on = models.CharField(default="", max_length=200)

class TotalDownloadsIOS(models.Model):
    country = models.CharField(default="", max_length=200)
    state = models.CharField(default="", max_length=200)
    region = models.CharField(default="", max_length=200)
    counting = models.PositiveIntegerField(default=0)
    last_downloaded_on = models.CharField(default="", max_length=200)

class SingleDownloadAndroid(models.Model):
    regionid = models.PositiveIntegerField(default=0)
    country = models.CharField(default="", max_length=200)
    state = models.CharField(default="", max_length=200)
    region = models.CharField(default="", max_length=200)
    email = models.EmailField(default="", max_length=200)
    phone_no = models.CharField(default="", max_length=200)
    downloaded_on = models.CharField(default="", max_length=200)

class SingleDownloadIOS(models.Model):
    regionid = models.PositiveIntegerField(default=0)
    country = models.CharField(default="", max_length=200)
    state = models.CharField(default="", max_length=200)
    region = models.CharField(default="", max_length=200)
    email = models.EmailField(default="", max_length=200)
    phone_no = models.CharField(default="", max_length=200)
    downloaded_on = models.CharField(default="", max_length=200)

class OnlineUsersAndroid(models.Model):
    online_user =models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    email = models.EmailField(default="", max_length=200, unique=True)
    country = models.CharField(default="", max_length=200)
    state = models.CharField(default="", max_length=200)
    region = models.CharField(default="", max_length=200)
    name = models.CharField(default="", max_length=200)
    phone_no = models.CharField(default="", max_length=200, unique=True)
    profile_type = models.CharField(default="", max_length=200)
    last_updated = models.DateTimeField(auto_now=True,null=True,blank=True)
    action = models.CharField(default="Active", max_length=200)
    current_users_count = models.PositiveIntegerField(default=0)

class OnlineUsersIOS(models.Model):
    email = models.EmailField(default="", max_length=200, unique=True)
    country = models.CharField(default="", max_length=200)
    state = models.CharField(default="", max_length=200)
    region = models.CharField(default="", max_length=200)
    name = models.CharField(default="", max_length=200)
    phone_no = models.CharField(default="", max_length=200, unique=True)
    profile_type = models.CharField(default="", max_length=200)
    last_updated = models.DateTimeField(auto_now=True)
    action = models.CharField(default="Active", max_length=200)
    current_users_count = models.PositiveIntegerField(default=0)

class Backup(models.Model):
    country = models.CharField(default="", max_length=200)
    state = models.CharField(default="", max_length=200)
    region = models.CharField(default="", max_length=200)
    name = models.CharField(default="", max_length=200)
    email = models.EmailField(default="", max_length=200)
    phone_no = models.CharField(default="", max_length=200)
    file_name = models.CharField(default="", max_length=200)
    last_updated = models.DateTimeField(auto_now=True)
    action = models.CharField(default="Active", max_length=200)

class Synchronisation(models.Model):
    country = models.CharField(default="", max_length=200)
    state = models.CharField(default="", max_length=200)
    region = models.CharField(default="", max_length=200)
    profile_type = models.CharField(default="", max_length=200)
    sync_frequency = models.CharField(default="", max_length=200)
    timeline = models.TimeField()
    action = models.CharField(default="Active", max_length=200)

class Restore(models.Model):
    country = models.CharField(default="", max_length=200)
    state = models.CharField(default="", max_length=200)
    region = models.CharField(default="", max_length=200)
    name = models.CharField(default="", max_length=200)
    email = models.EmailField(default="", max_length=200)
    phone_no = models.CharField(default="", max_length=200)
    file_name = models.CharField(default="", max_length=200)
    last_updated = models.DateTimeField(auto_now=True)
    action = models.CharField(default="Active", max_length=200)

from datetime import date
class Feedback(models.Model):
    feedback_user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    country = models.CharField(default="", max_length=200)
    state = models.CharField(default="", max_length=200)
    profile_type = models.CharField(default="", max_length=200)
    region = models.CharField(default="", max_length=200)
    name = models.CharField(default="", max_length=200)
    email = models.EmailField(default="", max_length=200)
    phone_no = models.CharField(default="", max_length=200)
    date = models.DateField(auto_now_add=True,null=True,blank=True)
    feedback = models.CharField(default="", max_length=3000)
    company_response = models.CharField(default="", max_length=3000)
    action = models.CharField(default="Active", max_length=200)

class Reviews(models.Model):
    reviews_user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    country = models.CharField(default="", max_length=200)
    state = models.CharField(default="", max_length=200)
    region = models.CharField(default="", max_length=200)
    profile_type = models.CharField(default="", max_length=200)
    name = models.CharField(default="", max_length=200)
    email = models.EmailField(default="", max_length=200)
    phone_no = models.CharField(default="", max_length=200)
    date = models.DateField(auto_now=True)
    review_rating = models.PositiveIntegerField(default="",null=True)
    review_comment = models.CharField(default="", max_length=3000)
    company_response = models.CharField(default="", max_length=3000)
    feedback_content = models.CharField(default="", max_length=3000)
    action = models.CharField(default="Active", max_length=200)

class ManageSubscription(models.Model):
    country = models.CharField(default="", max_length=200)
    subscription_plan = models.CharField(default="", max_length=200)
    profile_type = models.CharField(default="", max_length=200)
    currency = models.CharField(default="", max_length=200)
    amount = models.FloatField()
    subscription_type = models.CharField(default="", max_length=200)
    collection_method = models.CharField(default="", max_length=200)
    action = models.CharField(default="Active", max_length=200)

class Subscribers(models.Model):
    country = models.CharField(default="", max_length=200)
    state = models.CharField(default="", max_length=200)
    region = models.CharField(default="", max_length=200)
    name = models.CharField(default="", max_length=200)
    email = models.EmailField(default="", max_length=200)
    phone_no = models.CharField(default="", max_length=200)
    profile_type = models.CharField(default="", max_length=200)
    subscription_type = models.CharField(default="", max_length=200)
    collection_method = models.CharField(default="", max_length=200)
    collection_mode = models.CharField(default="", max_length=200)
    currency = models.CharField(default="", max_length=200)
    amount = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    action = models.CharField(default="Active", max_length=200)

class Support(models.Model):
    country = models.CharField(default="", max_length=200)
    state = models.CharField(default="", max_length=200)
    region = models.CharField(default="", max_length=200)
    name = models.CharField(default="", max_length=200)
    email = models.EmailField(default="", max_length=200)
    phone_no = models.CharField(default="", max_length=200)
    date = models.DateField(auto_now=True)
    subject = models.CharField(default="", max_length=200)
    issue_details = models.TextField()
    solution_provided = models.TextField()
    status = models.CharField(default="open", max_length=200)
    action = models.CharField(default="Active", max_length=200)

class ContactUs(models.Model):
    name = models.CharField(default="", max_length=200)
    email = models.EmailField(default="", max_length=200)
    phone_no = models.CharField(default="", max_length=200)
    message = models.TextField(default="")

class AboutUs(models.Model):
    heading = models.CharField(default="", max_length=200)
    content = models.TextField()
    vision = models.TextField()
    mission = models.TextField()
    action = models.CharField(default="Active", max_length=200)
    upload = models.ImageField(upload_to='media/about')

class Footer(models.Model):
    logo = models.FileField(upload_to='footer', default="")
    footer_description = models.CharField(default="", max_length=400)
    google_play_store_link = models.URLField(default="")
    facebook_page_link = models.URLField(default="")
    twitter_page_link = models.URLField(default="")
    pinterest_page_link = models.URLField(default="")
    linkedin_page_link = models.URLField(default="")
    action = models.CharField(default="Active", max_length=200)

class Header(models.Model):
    logo = models.FileField(upload_to='header', default="")
    header_title = models.CharField(default="", max_length=200)
    header_description = models.TextField()
    google_play_store_link = models.URLField(default="")
    action = models.CharField(default="Active", max_length=200)

class NavigationMenu(models.Model):
    nav_item = models.CharField(default="", max_length=200)
    nav_link = models.URLField(default="")
    action = models.CharField(default="Active", max_length=200)

class SliderHeader(models.Model):
    image = models.FileField(upload_to='slider-header', default="")
    title = models.CharField(default="", max_length=200)
    short_description = models.CharField(default="", max_length=300)
    call_to_action_link = models.URLField(default="")
    action = models.CharField(default="Active", max_length=200)

class Services(models.Model):
    category = models.CharField(default="", max_length=200)
    name = models.CharField(default="", max_length=200)
    image = models.FileField(upload_to='services', default="")
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)
    
class Product(models.Model):
    productname=models.CharField(default="", max_length=200)
    upload = models.ImageField(upload_to='media/product')
    heading1=models.CharField(default="", max_length=200)
    content1=models.TextField()
    content2=models.TextField()
    heading2=models.CharField(default="", max_length=200)
    content3=models.TextField()
    heading3=models.CharField(default="", max_length=200)
    content4=models.TextField()
    four_steps=models.CharField(default="", max_length=200)
    step1heading=models.CharField(default="", max_length=200)
    step1content=models.TextField()
    step2heading=models.CharField(default="", max_length=200)
    step2content=models.TextField()
    step3heading=models.CharField(default="", max_length=200)
    step3content=models.TextField()
    step4heading=models.CharField(default="", max_length=200)
    step4content=models.TextField()
    eligibility_content=models.TextField()
    criteria1=models.CharField(default="", max_length=200)
    criteria2=models.CharField(default="", max_length=200)
    criteria3=models.CharField(default="", max_length=200)
    criteria4=models.CharField(default="", max_length=200)
    action = models.CharField(default="Active", max_length=10)

class Retailer(models.Model):
    retailername=models.CharField(default="", max_length=200)
    upload = models.ImageField(upload_to='media/product')
    heading1=models.CharField(default="", max_length=200)
    content1=models.TextField()
    content2=models.TextField()
    heading2=models.CharField(default="", max_length=200)
    content3=models.TextField()
    heading3=models.CharField(default="", max_length=200)
    content4=models.TextField()
    four_steps=models.CharField(default="", max_length=200)
    step1heading=models.CharField(default="", max_length=200)
    step1content=models.TextField()
    step2heading=models.CharField(default="", max_length=200)
    step2content=models.TextField()
    step3heading=models.CharField(default="", max_length=200)
    step3content=models.TextField()
    step4heading=models.CharField(default="", max_length=200)
    step4content=models.TextField()
    eligibility_content=models.TextField()
    criteria1=models.CharField(default="", max_length=200)
    criteria2=models.CharField(default="", max_length=200)
    criteria3=models.CharField(default="", max_length=200)
    criteria4=models.CharField(default="", max_length=200)
    action = models.CharField(default="Active", max_length=10)


class Professional(models.Model):
    professionalname=models.CharField(default="", max_length=200)
    upload = models.ImageField(upload_to='media/product')
    heading1=models.CharField(default="", max_length=200)
    content1=models.TextField()
    content2=models.TextField()
    heading2=models.CharField(default="", max_length=200)
    content3=models.TextField()
    heading3=models.CharField(default="", max_length=200)
    content4=models.TextField()
    four_steps=models.CharField(default="", max_length=200)
    step1heading=models.CharField(default="", max_length=200)
    step1content=models.TextField()
    step2heading=models.CharField(default="", max_length=200)
    step2content=models.TextField()
    step3heading=models.CharField(default="", max_length=200)
    step3content=models.TextField()
    step4heading=models.CharField(default="", max_length=200)
    step4content=models.TextField()
    eligibility_content=models.TextField()
    criteria1=models.CharField(default="", max_length=200)
    criteria2=models.CharField(default="", max_length=200)
    criteria3=models.CharField(default="", max_length=200)
    criteria4=models.CharField(default="", max_length=200)
    action = models.CharField(default="Active", max_length=10)


class ManagementTeam(models.Model):
    name = models.CharField(default="", max_length=200)
    designation = models.CharField(default="", max_length=200)
    image = models.FileField(upload_to='footer', default="")
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class AdvisoryBoard(models.Model):
    name = models.CharField(default="", max_length=200)
    designation = models.CharField(default="", max_length=200)
    image = models.FileField(upload_to='footer', default="")
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class TermsAndConditions(models.Model):
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class TermsOfUse(models.Model):
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class FairPracticeCode(models.Model):
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class PrivacyPolicy(models.Model):
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class Disclaimer(models.Model):
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)


class RefundPolicy(models.Model):
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class GrievanceAddressMechanism(models.Model):
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class Faq(models.Model):
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class LifeAtAdfpay(models.Model):
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)


CHOICES = (
        ('Saving', ' Saving'),
        ('Current', 'Current'),
        ('Credit', 'Credit'),
    )
class Bankdetails(models.Model):
    bank_user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    account_holder_name = models.CharField(max_length=50)
    account_number = models.IntegerField()
    bank_name = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=20)
    account_type = models.CharField(default="",max_length=300)
    photo = models.FileField(upload_to='documents/pdf')
