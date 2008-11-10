
# /wiki/urls.py - kernel1983
#
# Copyright (c) 2007 kernel1983@gmail.com
# Distributed under the BSD License
#


from django.conf.urls.defaults import *

urlpatterns = patterns('wiki.views',
    (r'^edit/$', 'error'),
    (r'^edit/(?P<title>.+)/$', 'edit'),
    (r'^history/$', 'error'),
    (r'^history/(?P<title>.+)/(?P<version>\d+)/$', 'history'),
    (r'^history/(?P<title>.+)/$', 'history'),
    (r'^(?P<title>.+)/$', 'topic'),
    (r'^$', 'topic'),
)
