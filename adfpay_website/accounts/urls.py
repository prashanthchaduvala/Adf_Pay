from django.urls import path
from .accounts_views import *

urlpatterns = [
    path("", user_login1, name="user_login1"),
    path('login1/', user_login1, name="user_login1"),
    path('logout1/', user_logout1, name='logout1'),
]