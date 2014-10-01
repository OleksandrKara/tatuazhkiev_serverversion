#coding: utf-8

from django.conf.urls import patterns, url
from tatuazhkiev.articles.views import PostsListView, PostDetailView 

urlpatterns = patterns('',
url(r'^$', PostsListView.as_view(), name='list'), # �� ���� �� URL http://���_�����/blog/ 
                                               # ����� ���������� ������ ������
url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()), # � �� URL http://���_�����/blog/�����/ 
                                              # ����� ���������� ���� � ������������ �������

)