from django.conf.urls import patterns, url

from matcher import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<hacker_id>\d+)/$', views.detail, name='detail'),
)
