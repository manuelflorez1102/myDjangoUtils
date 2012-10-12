from django.conf.urls import patterns, include, url

urlpatterns = patterns('books.views',
    url(r'^$', 'index'),
    url(r'^cookie/$', 'show_color'),
    url(r'^set_cookie/$', 'set_color'),
)
