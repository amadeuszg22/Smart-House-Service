from django.conf.urls import url, include
#from django.urls import path
#from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #url('', views.List.as_view()),
    url('chanellist', views.ChannelList.as_view()),
    url('chanellist/<int:pk>/', views.ChannelDetail.as_view()),
    url('devlist', views.DevList.as_view()),
    url('devlist/<int:pk>/', views.DevDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)