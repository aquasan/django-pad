from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    # Example:
    # (r'^djangocn/', include('djangocn.foo.urls')),
    (r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    (r'^wiki/', include('wiki.urls')),
    (r'^$', 'wiki.views.topic'),

    (r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'account/login.html'},),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'account/logout.html'},),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
