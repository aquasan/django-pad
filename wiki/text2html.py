
#--------------------------------------------------------
#
# copy from woodlog at www.djangocn.org by limodou
#
#--------------------------------------------------------

import re
import cgi

re_string = re.compile(r'(?P<htmlchars>[<&>])|(?P<space>^[ \t]+)|(?P<lineend>\r\n|\r|\n)|(?P<protocal>\b((http|ftp)://.*?))(\s|$)',    re.S|re.M|re.I)

def text2html(text):
    '''called for comments'''
    def do_sub(m):
        c = m.groupdict()
        if c['htmlchars']:
            return cgi.escape(c['htmlchars'])
        if c['lineend']:
            return '<br>'
        elif c['space']:
            t = m.group().replace('\t', '&nbsp;'*4)
            t = t.replace(' ', '&nbsp;')
            return t
        elif c['space'] == '\t':
            return ' '*4;
        else:
            last = m.groups()[-1]
            if last in ['\n', '\r', '\r\n']:
                last = '<br>'
            return '<a href="%s">%s</a>%s' % (c['protocal'], c['protocal'], last)
    return re.sub(re_string, do_sub, text)


def plain2html(text):
    '''called when edit or new post'''
    html = text.strip()

    #html = html.replace('&lt;','&amp;lt;')
    #html = html.replace('&gt;','&amp;gt;')

    html = html.replace('<','&lt;')
    html = html.replace('>','&gt;')

    return html


def rt2br(text):
    '''return to <br> and it is called before diaplay'''

    html = text
    l = None

    if html.find('\r\n') != -1:
        l = html.split('\r\n')

    elif html.find('\n') != -1:
        l = html.split('\n')

    elif html.find('\r') != -1:
        l = html.split('\r')

    if isinstance(l,list):

        i = 0
        #print l
        del_next = True

        for i in range(len(l)):
            if(l[i] == ''):
                l[i] = '<br>'

        '''
        while(i != len(l)):
            if(l[i] == ''):# or l[i] == '\n'):
                if(del_next):
                    del_next = False
                else:
                    l[i] = '<br>'
            else:
                del_next = True
            i+=1
        '''
        #print l
        html = '\n'.join(l)


    html = html.replace('\\<','&lt;')
    html = html.replace('\\>','&gt;')

    return html


if __name__=='__main__':
    #print rt2br('<pre>hello:\n    zzz</pre>aaa\naaa\n\naaa\n')
    print plain2html('<pre>hello:\n    zzz</pre>aaa\naaa\n\naaa\n')