from django.conf.urls import include, url
from django.conf.urls import patterns
from . import views

urlpatterns = patterns ('messege.views',
(r'^$', 'messege_list' ),)
