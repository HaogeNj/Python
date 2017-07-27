# -*- coding:utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 头部信息，模拟浏览器访问
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'}

f = open('C:\Users\Administrator\PycharmProjects\charcount\poem\indexurl.txt', 'r')
poemdata = open('C:\Users\Administrator\PycharmProjects\charcount\poem\poemdata.txt', 'w')

#异常数据应该追加写入
errordata = open('C:\Users\Administrator\PycharmProjects\charcount\poem\erroedata.txt', 'a')

x = 0

try:
    while 1:
        line = f.readline().strip('\n')

        if not line:
            break

        try:
            req = urllib2.Request(line, headers=headers)  # 创建对象
            page = urllib2.urlopen(req, timeout=200)  # 设置超时
            contents = page.read()

            soup = BeautifulSoup(contents, 'html.parser')
            gettitle =  soup.find(id='middlediv').find('h2').text.strip()  # 标题
            dynasty = soup.find(attrs={'class': 'jjzz'}).find_all()[0].text.strip()  # 年代
            author = soup.find(attrs={'class': 'jjzz'}).find_all()[1].text.strip()   # 作者
            poemcontent =  soup.find(attrs={'class': 'shicineirong'}).text.strip().replace('\n','')  # 古诗内容

            #输出诗词标题+朝代+作者+内容
            poemdata.write(gettitle +'|$|' + dynasty + '|$|' + author + '|$|' + poemcontent + '|$|' + line + '\n')

            x +=1

            if x%1000 == 0:
                print 'current get poem num:' + str(x)

        except Exception, e:
            print e
            errordata.write(line+'\n')
finally:
    f.close()
    poemdata.close()

print 'download over'


