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
]
