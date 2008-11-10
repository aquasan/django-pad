from django.db import models
import datetime

class Topic(models.Model):
    title = models.CharField(max_length=255, blank=True)
    time = models.DateTimeField(default = datetime.datetime.now(), blank=True)
    body = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255, blank=True)
    user = models.CharField(max_length=255, blank=True)
    #last = models.IntegerField(default=0, blank=True)

    class Meta:
        ordering = ('-id',)

    class Admin:
        list_display = ('category', 'title', 'time', 'body', 'user')
