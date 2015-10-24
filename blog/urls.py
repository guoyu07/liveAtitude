# coding:utf-8
__author__ = 'albert'

from django.conf.urls import include, url
from django.contrib import admin
from blog.views import Home, Detail
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home.as_view()),
    url(r'^article/(?P<slug>\d+).html$', Detail.as_view()),
]