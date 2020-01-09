from pyquery import PyQuery as pq
import requests
import json
from pprint import pprint
import os


class KKPrint(object):
    # 定义构造方法
    def __init__(self, title,info, author, time, zh, en, herf):
        # 设置属性
        self.title = title
        self.info = info
        self.author = author
        self.time = time
        self.zh = zh
        self.en = en
        self.herf = herf
    
    def Page(self):
        # 将网址对应页面标签中的部分内容存储起来
        pageurl = self.herf
        r = requests.get(pageurl)
        r.encoding = 'utf-8'
        pagehtml = r.text
        # print(pagehtml)
        html = pq(pagehtml)
        article = html("#article")
        item = article.html() # 所有内容
        it = pq(item)
        # print(it)
        en = it(".qh_en").text() # 英文内容全部以qh_en为标签属性 
        zh = it(".qh_zg").text()
        self.en = en
        self.zh = zh
        # print(en,zh)
    
    def KKCout(self):
        # 转成字典类型
        KKdict = {}
        KKdict['title'] = self.title
        KKdict['author'] = self.author
        KKdict['time'] = self.time
        KKdict['info'] = self.info
        KKdict['zh'] = self.zh
        KKdict['en'] = self.en
        return KKdict
        
        

def Save(text):
    if 'sort' not in os.listdir():
        os.mkdir('sort')
    os.chdir(r'.\sort')
    saveall = open('text.txt','w',encoding='utf-8')
    saveall.write(text)
 
      
url = 'http://www.kekenet.com/read/news/keji/'
r = requests.get(url)
r.encoding = 'utf-8' #解决乱码问题
indexhtml = r.text
# print(indexhtml)
indexh = pq(indexhtml)
lists1 = indexh("#menu-list h2")
lists2 = indexh("#menu-list li")
# for li in lists1.items():
#     print(li.text())
sort = []
i = 0
for li2 in lists2.items():
    p = li2("p")
    # a = li2("a").attr.herf 空值？
    b = li2("h2")
    a = b("a") #<a></a> 标签中含有文字
    c = li2.remove("a") #移除a中已经打印的内容
    i += 1
    # print(i, a.attr.href, a.text(),p.text()[:-13],p.text()[-12:-4],c.text()[:-23])
    # __init__(self, title,info, author, time, zh, en, herf)
    d = KKPrint(a.text(),c.text()[:-23],p.text()[-9:-4],p.text()[:-13],'','',a.attr.href) # 定义一d个类
    # d.herf = a.attr.href
    # d.title = a.text()
    # d.time = p.text()[:-13]
    # d.info = c.text()[:-23]
    # d.author = p.text()[-12:-4]
    d.Page()
    sort.append(d.KKCout())
# print(sort)
json = json.dumps(sort, ensure_ascii=False)
# pprint(json)(没什么用)
# print(json)
Save(json)

    