from django.conf.urls import include, url
from django.conf.urls import patterns
from . import views


urlpatterns = patterns ('Documents.views',
(r'^zwolnienie_new$', 'zwolnienie_new'),
(r'^$', 'docs_list'),
(r'^patron_new$', 'patron_new'),
(r'^(?P<pk>[0-9]+)/removre$', 'docs_remove'),
(r'^(?P<pk>[0-9]+)/edit$', 'docs_edit'),
(r'^(?P<pk>[0-9]+)/generate$', 'docs_generate'),
(r'^(?P<pk>[0-9]+)/patron_edit$', 'patron_edit'),
(r'^(?P<pk>[0-9]+)/zwolnienie_edit$', 'zwolnienie_edit'),
(r'^(?P<pk>[0-9]+)/zwolnienie_generate$', 'zwolnienie_generate'),
(r'^(?P<pk>[0-9]+)/patron_generate$', 'patron_generate'),

)