# -*- coding:utf-8 -*-

import urllib2,urllib
import re
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://www.dbmeinv.com/dbgroup/show.htm?pager_offset=1"
x = 0

def crawl(url):
    #头部信息，模拟浏览器访问
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'}
    req = urllib2.Request(url,headers=headers)  #创建对象
    page = urllib2.urlopen(req,timeout=200)  #设置超时
    contents = page.read()
    #print contents

    soup = BeautifulSoup(contents,'html.parser')
    my_girl = soup.findAll('img')

    for girl in my_girl:
        link = girl.get('src')
        global x
        urllib.urlretrieve(link, 'image\%s.jpg'%x)
        x += 1  #没有++的写法
        print link + '    正在下载第%s张'%x

for page in range(1,100):

    url = 'http://www.dbmeinv.com/dbgroup/show.htm?pager_offset=%s'%page
    #url = 'http://www.dbmeinv.com/dbgroup/show.htm?pager_offset=%d' % page
    #url = 'http://www.dbmeinv.com/dbgroup/show.htm?pager_offset={}'.format(page)
    print url
    crawl(url)

print 'download over'


