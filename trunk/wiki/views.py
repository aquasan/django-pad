import datetime

from django.template import loader, Context
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required

from models import *
from text2html import *
from wiki2html import tag2link
import settings as wiki_settings

import merge3


def topic(request, title = wiki_settings.front_page):
    th = Topic.objects.filter(title = title)
    if len(th):
        content = tag2link(rt2br(plain2html(th[0].body)))
        css = ''
        mtime = datetime.datetime.ctime(th[0].time)
    else:
        content = ''
        css = ''
        mtime = ''

    if len(content):
        c = Context()
        c['user'] = request.user
        c['title'] = title
        c['css'] = css
        c['content'] = content
        c['mtime'] = mtime

        return render_to_response('wiki/display.html', c)
    else:
        if request.user.is_anonymous():
            c = Context()
            c['title'] = 'No found'
            return render_to_response('wiki/no_found.html', c)
        else:
            return HttpResponseRedirect('/wiki/edit/' + title + '/')

@login_required
def edit(request, title = wiki_settings.front_page):
    if request.method == 'POST' and request.POST.has_key('content') and request.POST.has_key('last'):
        content = request.POST['content']
        last_id = request.POST['last']

        th = Topic.objects.filter(title = title)
        th2 = th.filter(id = last_id)

        if len(th):
            recent_id = str(th[0].id)
            recent_content = th[0].body
        else:
            recent_id = '0'
            recent_content = ''

        if len(th2):
            last_content = th2[0].body
        else:
            last_content = ''

        preview = tag2link(rt2br(plain2html(content)))

        if content == recent_content:
            c = Context()
            c['user'] = request.user
            c['title'] = title
            c['preview'] = preview
            c['content'] = content
            c['last'] = recent_id
            c['msg'] = 'No Changes!'

            return render_to_response('wiki/edit.html', c)

        if recent_id != last_id:
            #differ function
            merger = merge3.Merge3(last_content, content, recent_content)
            content = "".join( [i for i in merger.merge_lines()] )

            c = Context()
            c['user'] = request.user
            c['title'] = title
            c['content'] = content
            c['last'] = recent_id
            c['msg'] = 'Conflict!'

            return render_to_response('wiki/edit.html', c)

        t = Topic(title = title, body = content, user = request.user.username)
        t.save()

        th = Topic.objects.filter(title = title)
        current_id = str(th[0].id)

        if content == '':
            c = Context()
            c['user'] = request.user
            c['title'] = title
            c['preview'] = preview
            c['content'] = content
            c['last'] = current_id
            c['msg'] = 'Deleted!'

            return render_to_response('wiki/edit.html', c)

        c = Context()
        c['user'] = request.user
        c['title'] = title
        c['preview'] = preview
        c['content'] = content
        c['last'] = current_id
        c['msg'] = 'Saved!'

        return render_to_response('wiki/edit.html', c)

    else:
        th = Topic.objects.filter(title = title)

        if len(th):

            content = th[0].body
            recent_id = str(th[0].id)
        else:
            content = ''
            recent_id = '0'

        c = Context()
        c['user'] = request.user
        c['title'] = title
        c['content'] = content
        c['last'] = recent_id
        
        return render_to_response('wiki/edit.html', c)

@login_required
def history(request, title = wiki_settings.front_page, version = None):
    c = Context()
    c['content'] = ''
    
    th = Topic.objects.filter(title = title)
    th2 = th
    if version:
        th2 = th2.filter(id = version)

    if th:
        c['range'] = [i.id for i in th]
    else:
        c['range'] = []

    if th2:
        c['content'] = tag2link(rt2br(th2[0].body))

        c['author'] = th2[0].user
        c['mtime'] = datetime.datetime.ctime(th2[0].time)
    else:
        c['content'] = ''

    c['user'] = request.user
    c['title'] = title

    return render_to_response('wiki/history.html', c)

def error(request):
    return HttpResponseNotFound('error')
