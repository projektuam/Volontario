from django.conf.urls import include, url
from django.conf.urls import patterns
from . import views


urlpatterns = patterns ('Users.views',
url(r'^register/$', views.register, name='register'),
url(r'^logout/$', views.user_logout, name='logout'),
url(r'^account/$', views.user_account ),
url(r'^account_setting/$', views.user_list ),
url(r'^(?P<usr>[0-9]+)/set_us/$', views.setting_account ),
url(r'^(?P<usr>[0-9]+)/user_edit/$', views.user_edit ),
url(r'^(?P<usr>[0-9]+)/user_remove/$', views.user_remove ),
)
