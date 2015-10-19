# coding:utf-8

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

# 用于修改admin中显示的app名称
class string_with_title(str):
    def __new__(cls, args, title):
        instance = str.__new__(cls, args)
        instance._title = title
        return instance


class Article(models.Model):
    title = models.CharField(max_length=100)  # 博客标题
    category = models.CharField(max_length=50, blank=True)  # 博客标签
    date_time = models.DateTimeField(auto_now_add=True)  # 博文日期
    content = models.TextField(blank=True, null=True) # 博客正文

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://127.0.0:8000%s" % path

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = verbose_name = u'文章'
        ordering = ['-date_time']
        app_label = string_with_title('blog', u'博客管理')

