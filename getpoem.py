# -*- coding:utf-8 -*-

import urllib2,urllib
import re
from bs4 import BeautifulSoup
import io
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://so.gushiwen.org/type.aspx?p=1&c=%E5%94%90%E4%BB%A3"
x = 0
chaodai = ['%e5%85%88%e7%a7%a6','%e4%b8%a4%e6%b1%89','%e9%ad%8f%e6%99%8b','%e5%8d%97%e5%8c%97%e6%9c%9d','%e9%9a%8b%e4%bb%a3','%e5%94%90%e4%bb%a3','%e4%ba%94%e4%bb%a3','%e5%ae%8b%e4%bb%a3','%e9%87%91%e6%9c%9d','%e5%85%83%e4%bb%a3','%e6%98%8e%e4%bb%a3','%e6%b8%85%e4%bb%a3']

def crawl(url):
    #头部信息，模拟浏览器访问
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'}
    req = urllib2.Request(url,headers=headers)  #创建对象
    page = urllib2.urlopen(req,timeout=200)  #设置超时
    contents = page.read()
    #print contents

    soup = BeautifulSoup(contents,'html.parser')
    my_poem = soup.findAll('textarea')
    ilen = len(my_poem)

    for i in range(ilen):
        istr = my_poem[i].string
        print istr
        f.write(istr + '\n')

f = open('C:\Users\Administrator\PycharmProjects\charcount\poem\\tangshi.txt', 'w')
for cd in chaodai:
    for page in range(1, 502):
        url = 'http://so.gushiwen.org/type.aspx?p={}'.format(page)+'&c='+ cd
        crawl(url)
f.close()

print 'download over'


