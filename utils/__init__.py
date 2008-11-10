

'''
def cutString(s, length):
    us = unicode(s, 'utf-8')
    
    n = int(length)
    t = us[:n]
    while True:
        try:
            t.encode('gb2312')
            break
        except:
            n -= 1
            t = us[:n]
    return t

def cutString_old(s, length):
    us = unicode(s, 'utf-8')
    gs = us.encode('gb2312')
    
    n = int(length)
    t = gs[:n]
    while True:
        try:
            unicode(t, 'gbk')
            break
        except:
            n -= 1
            t = gs[:n]
    return t.decode('gb2312')
'''

if __name__=='__main__':
    print cutString('aa\xef\xbb\xbfddeeefff',5)
    #print cutString_old('aa\xef\xbb\xbfddeeefff',5)
