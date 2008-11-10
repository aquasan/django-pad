#!/home/kernel1983/bin/python
import sys

#sys.stderr = open('err.log','w')
#sys.path += ['/home/jcroft/django/django_src']

sys.path += ['/home/kernel1983/www.djangocn.com']
sys.path += ['/home/kernel1983/www.djangocn.com/djangocn']

from fcgi import WSGIServer
from django.core.handlers.wsgi import WSGIHandler

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangocn.settings'
WSGIServer(WSGIHandler()).run()
