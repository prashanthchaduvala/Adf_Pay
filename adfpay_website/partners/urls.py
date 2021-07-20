from django.urls import path
from partners import views
appname='partner'
urlpatterns = [
    path('', views.index, name='index'),
    path('partner', views.index, name='partnerdashboard'),
    path('usersave/',views.usersave,name='usersave'),

    # downloads
    path('downloadpartner/', views.download, name='downloadpartner'),
    # onlineuser
    path('onlineuserpartner/', views.onlineuser, name='onlineuserpartner'),
    # client aquasization
    path('aquasization/', views.aquasization, name='aquasization'),
    # userprofile
    path('userprofile/', views.userprofile, name='userprofile'),

    # ReferallPartner
    path('referallpartner/',views.referallpartner,name='referallpartner'),
    # Commision
    path('commision/', views.commision, name='commision'),

    # Approved Rate
    path('approvedrate/', views.approvedrate, name='approvedrate'),

    # countheader
    path('countheader/', views.countheader, name='countheader'),

    # logout
    path('logoutpartner/',views.logoutpartner, name='logoutpartner'),
    path('log/', views.log, name='log'),
    path('partnerlogin/',views.partnerlogin,name='partnerlogin'),
    path('loginuser/',views.loginuser,name='loginuser')


]
