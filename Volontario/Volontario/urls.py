from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
url(r'^events/', include('Event.urls')),
url(r'^admin/', include(admin.site.urls)),
url(r'^ind/', include('Ind.urls')),
url(r'^summernote/', include('django_summernote.urls')),
url(r'^reg/', include('Users.urls')),
url(r'^doc/', include('Documents.urls')),
url(r'^', include('Actuall.urls')),
url(r'^reset/password_reset/$', 'django.contrib.auth.views.password_reset', name='reset_password_reset1'),
url(r'^reset/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

]
