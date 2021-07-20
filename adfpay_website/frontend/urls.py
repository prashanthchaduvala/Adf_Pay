from django.urls import path,re_path
from django.conf.urls import url
from .views import *

app_name = 'frontend'

urlpatterns = [
    path('', index, name='index'),
    path('', index, name='frontendindex'),
    path('about/', about, name='about'),
    re_path(r'^blog/$', blog, name='blog'),
    # url(r'^blog_detail/(?P<id>[0-9]+)/$', blog_detail, name='blog_detail'), 
    path('blog_detail/<str:id>/', blog_detail, name='blog_detail'),
    path('employees/', employees, name='employees'),
    path('add_country_code/', add_country_code, name='add_country_code'),
    path('profession/', profession, name='profession'),
    path('retailer/', retailer, name='retailer'), 
    path('profession_detail/<str:id>/', profession_detail, name='profession_detail'),
    path('employees_details/<str:id>/', employees_details, name='employees_details'),
    # url(r'^employees_details/(?P<id>[0-9]+)$', employees_details, name='employee_detail'),
    # path('service_employee/',service_employee, name='service_employee'),
    path('retailer_details/<str:id>/', retailer_details, name='retailer_details'),
    # path('blog/<int:id>/', blog_detail, name='blog_detail'),
    path('news-event/', news_event, name='news_event'),
    path('download_app/', download_app, name='download_app'),
    path('news-event-details/<str:id>/', news_event_detail, name='news_event_detail'),
    path('services/', services, name='services'),
    path('sign-in/', sign_in, name='sign_in'),
    path('partner_login/', partner_login, name='partner_login'),
    path('become_partner/', become_partner, name='become_partner'),
    path('sign-in-download/', sign_in_download, name='sign_in_download'),
    path('sign-up/', sign_up, name='sign_up'),
    path('contact/', contact, name='contact'),
    path('services/<str:category>/<int:id>/', service_detail, name='service_detail'),
    path('career/', career, name='career'),
    path('applyjob/<int:id>/', apply_career, name='applyjob'),
    path('apply-job/', apply_job, name='apply-job'),
    path('adfpay/<str:objectType>/', footer_contents, name='footer_contents'),
    path('team-members/', manage_team, name='manage_team'),
    path('advisory-board/', advisory_board, name='advisory_board'),
    path('send-message/', sendmessage, name='sendmessage'),
]
