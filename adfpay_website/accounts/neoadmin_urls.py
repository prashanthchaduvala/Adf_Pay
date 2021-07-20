from django.urls import path
from .neoadmin_views import *

urlpatterns = [
    
    path('', dashboard, name='neoadmin'),
    path('dashboard/', dashboard, name='dashboard'),
    path('permission/', permission, name='permission'),
    path('permission_users/', permission_users, name='permission_users'),
    path('change_action/<str:objectType>/<int:objectId>/', change_action, name='change_action'),
    path('show_object_list/<str:objectType>/', show_object_list, name='show_object_list'),
    path('model_object/<str:objectType>/', model_object, name='model_object'),
    path('saveObject/<str:objectType>/', saveObject,name='saveObject'),
    path('updateObject/<str:objectType>/<int:objectId>/', updateObject,name='updateObject'),
    path('deleteObject/<str:objectType>/<int:objectId>/', deleteObject,name='deleteObject'),
    path('test/', test, name='test'),
]


