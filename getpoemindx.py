# -*- coding:utf-8 -*-

'''
古诗文网站全部诗词下载
1.整体思路是根据作者找到相关的作品列表
2.遍历列表清单，下载诗词内容，包含标题、朝代、作者、诗词内容
3.实现方案分解为2个脚本，第一个下载索引，因为诗词list的数据可能有好几百万，直接遍历不是很好。先获取到有效的list。再进行内容下载。
注意：
网站分页有限制，每个作者的翻页只有100页，所以可能陆游的诗词下不完整的，其他的还需要验证。
检查网站，应该只有13073个作者。

数据爬取时间
2017-07-26
'''

import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://www.shicimingju.com/chaxun/zuozhe/1_1.html"
x = 0

reg = r'<li>.+?《<a href="(/chaxun/list/.+?.html)"'
poemre = re.compile(reg)

#首先回去诗词展示页面的地址
def crawl(url):
    #头部信息，模拟浏览器访问
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'}

    try:
        req = urllib2.Request(url, headers=headers)  # 创建对象
        page = urllib2.urlopen(req, timeout=200)  # 设置超时
        contents = page.read()

        poemlist = re.findall(poemre, contents)

        ilen = len(poemlist)
        for i in range(ilen):
            url2 = 'http://www.shicimingju.com' + poemlist[i]
            global x
            x +=1
            f.write(url2 + '\n')

    except Exception, e:
        global iloop2
        iloop2 = 103

f = open('C:\Users\Administrator\PycharmProjects\charcount\poem\indexurl.txt', 'w')

#获取索引页面地址
for poet in range(1,13074):
    print 'strat getting '+str(poet)

    iloop2 = 1
    while iloop2 < 102:
        poeturl = 'http://www.shicimingju.com/chaxun/zuozhe/' + str(poet) + '_' + str(iloop2) + '.html'
        iloop2 +=1
        crawl(poeturl)

    print 'current url is ' + str(x)
f.close()

print 'download over'


