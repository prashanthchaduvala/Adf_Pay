from django.urls import path,include
from .views import *
from django.conf.urls import *

app_name = 'api'

urlpatterns=[
    path('ManageNewsMedia/', ManageNewsMediaAPIView.as_view(),name='ManageNewsMedia_list'),
    path('ManageNewsMedia/<int:id>/', ManageNewsMediaAPIView.as_view(),name='ManageNewsMedia_operation'),

]
