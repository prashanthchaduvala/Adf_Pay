from django.urls import path
from .accounts_views import *

urlpatterns = [
    path("", user_login, name="user_login_new"),
    path("create_staff_member/", create_internal_user, name="create_internal_user"),
    path("update_staff_member/<int:id>/", update_internal_user, name="update_internal_user"),
    path("login/", user_login, name="user_login"),
    path('logout/', user_logout, name='logout'),
    path('logout3/', user_logout, name='logout3'),
    path('forgotpassword/', forgot_password, name='forgot_password'),
    path('recoverpassword/', recover_password, name='recover_password'),
]
