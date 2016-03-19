from django.conf.urls import include, url
from django.conf.urls import patterns
from . import views


urlpatterns = patterns ('Documents.views',
(r'^zwolnienie_new$', 'zwolnienie_new'),
(r'^$', 'docs_list'),
(r'^patron_new$', 'patron_new'),
)