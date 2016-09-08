from django.conf.urls import patterns, url


from . import views


urlpatterns = patterns('',
    url(r'^anypost/$', views.anypost),
    url(r'^fivehundred/$', views.fivehundred),
    url(r'^hundred/$', views.hundred),
    url(r'^thousand/$', views.thousand),
    url(r'^threethousand/$', views.threethousand),
)
