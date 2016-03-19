from django.conf.urls import include, url
from django.conf.urls import patterns
from . import views


urlpatterns = patterns ('Ind.views',
(r'^$', 'volin_list'),
(r'^new$', 'volin_new'),
(r'^(?P<pk>[0-9]+)/$', 'volin_detal'),
(r'^(?P<pk>[0-9]+)/rem$', 'volin_remove'),
(r'^(?P<pk>[0-9]+)/edit$', 'volin_edit'),
(r'^(?P<pk>[0-9]+)/add_user$', 'volin_user'),
(r'^(?P<pk>[0-9]+)/(?P<usr>[0-9]+)/remove_user/$', 'user_remove'),
)

