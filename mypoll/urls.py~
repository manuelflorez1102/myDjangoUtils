from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
    url(r'^polls/', include('polls.urls')),
    url(r'^books/', include('books.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
