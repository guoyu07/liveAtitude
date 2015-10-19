# coding:utf-8
__author__ = 'albert'

from django.conf.urls import include, url
from django.contrib import admin
from blog.views import home, detail
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^(?P<id>\d+)/$', detail, name='detail'),
]