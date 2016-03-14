from django.conf.urls import include, url
from django.conf.urls import patterns
from . import views


urlpatterns = patterns ('Users.views',
url(r'^register/$', views.register, name='register'),
url(r'^logout/$', views.user_logout, name='logout'),
)
