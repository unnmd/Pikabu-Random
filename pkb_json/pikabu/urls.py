from django.conf.urls import patterns, url


from . import views


urlpatterns = patterns('',
    url(r'^anypost&pron=(?P<pron>[0-1]{1})&my=(?P<my>[0-1]{1})/$', views.anypost),
    url(r'^fivehundred&pron=(?P<pron>[0-1]{1})&my=(?P<my>[0-1]{1})/$', views.fivehundred),
    url(r'^hundred&pron=(?P<pron>[0-1]{1})&my=(?P<my>[0-1]{1})/$', views.hundred),
    url(r'^thousand&pron=(?P<pron>[0-1]{1})&my=(?P<my>[0-1]{1})/$', views.thousand),
    url(r'^threethousand&pron=(?P<pron>[0-1]{1})&my=(?P<my>[0-1]{1})/$', views.threethousand),
)
