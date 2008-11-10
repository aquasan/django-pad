#!/usr/bin/env python
# encoding: utf-8
"""
wiki2html.py

Created by kernel1983 on 2007-05-23.
"""

import re
import string

def is_url(text):
    prefix_list = ('http://','https://','ftp://','telnet://','mailto:','skype:')
    for i in prefix_list:
        if text.startswith(i):
            return True
    return False

def is_img(text):
    ext_list = ('.png','.jpg','.gif','.bmp')
    for i in ext_list:
        if text.endswith(i):
            return True
    return False

def tag2link(text):
    #please be sure there is no <> in text
    #call plain2html before this fun

    c = text

    c = c.replace('[', '[<')
    c = c.replace(']', '>]')

    lines = re.split(r'\[|\]', c)
    #print l

    for i in range(len(lines)):
        if re.match(r'<(.*?)>', lines[i]):
            link = lines[i].strip('<').strip('>')
            link = link.split()

            if len(link) == 1:
                if is_img(link[0]):
                    head = ''
                    tail = ''
                    link[0] = '<img src="'+link[0]+'" />'
                elif is_url(link[0]):
                    head = '<a href="'+link[0]+'">'
                    tail = '</a>'
                else:
                    head = '<a href="/wiki/'+link[0]+'">'
                    tail = '</a>'
                link.insert(0, head)
                link.insert(2, tail)

                lines[i] = ''.join(link)

            else:    
                head = link.pop(0)
                if is_url(head):
                    head = '<a href="'+head+'">'
                    tail = '</a>'
                #elif is_img(head):
                    #head = '<img src="'+head+'">'
                    #tail = '</img>'
                else:
                    head = '<a href="/wiki/'+head+'">'
                    tail = '</a>'

                lines[i] = ' '.join(link)
                lines[i] = head + lines[i] + tail

    c = ''.join(lines)

    return c

if __name__=='__main__':
    #print tag2link('[mailto:kernel1983@gmail.com email]cc')
    print tag2link('aaa[  中文 ccc  s zzz]z[z z|1 1]z')
    print tag2link('aaa[http://text/ ccc]z[z]z')
    print tag2link('aaa[http://text.png]')
    #print tag2link('aaa[http://text/]z[z]z')

