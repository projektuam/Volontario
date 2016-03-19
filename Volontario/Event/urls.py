from django.conf.urls import include, url
from django.conf.urls import patterns
from . import views


urlpatterns = patterns ('Event.views',
(r'^$', 'event_list'),
(r'^tasks$', 'task_list'),
(r'^new/$', 'event_new'), 
(r'^(?P<pk>[0-9]+)/$', 'event_detal'),
(r'^(?P<pk>[0-9]+)/edit$', 'event_edit'),
(r'^(?P<pk>[0-9]+)/rem$', 'event_remove'),
(r'^(?P<pk>[0-9]+)/new_task/$', 'new_task'),
(r'^(?P<pk>[0-9]+)/(?P<task_id>[0-9]+)/task_remove$', 'task_remove'),
(r'^login/$',  'login_user'), 
(r'^(?P<pk>[0-9]+)/add/$', 'event_user'),
(r'^(?P<pk>[0-9]+)/(?P<usr>[0-9]+)/remove_user/$', 'user_remove'),
(r'^(?P<pk>[0-9]+)/(?P<task_id>[0-9]+)/add_user_task/$', 'user_task'),
(r'^(?P<pk>[0-9]+)/(?P<usr>[0-9]+)/(?P<tk>[0-9]+)/remove_user_task/$', 'user_remove_task'),
(r'^(?P<pk>[0-9]+)/(?P<task_id>[0-9]+)/$', 'user_view'),

)

