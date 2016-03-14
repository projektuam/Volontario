from django.conf.urls import include, url
from django.conf.urls import patterns
from . import views


urlpatterns = patterns ('Documents.views',
(r'^new$', 'new'),
(r'^$', 'docs_list'),
(r'^zwolnienie$', 'zwolnienie'),

)




