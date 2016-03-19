from django.conf.urls import include, url
from django.conf.urls import patterns
from . import views


urlpatterns = patterns ('Actuall.views',
(r'^$', 'aktual_list'),
(r'^nowy/$', 'aktual_new'), 
(r'^(?P<pk>[0-9]+)/edit$', 'aktual_edit'),
(r'^(?P<pk>[0-9]+)/usun$', 'aktual_remove'),
(r'^(?P<pk>[0-9]+)/detal$', 'aktual_detal'),
)
