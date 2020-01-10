# 作业要求：不只是爬取第一页，需要分析分页链接，并爬取尽可能多的列表页
# 对于爬取的文章页面，要求解析尽可能多的结构化数据，比如标题、作者、来源、时间、分类、标签、中英文文本等
from pyquery import PyQuery as pq
import requests
import json
from pprint import pprint
import os
from pymongo import MongoClient

sorturl = []

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
        if en == '':
            en = it("#article_eng").text()
        if zh == '':
            zh = it("#article_eng").text()
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
        
        

def Save(kkdict, my_set):
      my_set.insert_many(kkdict)


# 处理一个页面下的所有文章
def OnePage(url,my_set):
      r = requests.get(url)
      r.encoding = 'utf-8' #解决乱码问题
      indexhtml = r.text
      # print(indexhtml)
      indexh = pq(indexhtml)
      lists1 = indexh("#menu-list h2")
      lists2 = indexh("#menu-list li")
      sort = []
      i = 0
      for li2 in lists2.items():
          p = li2("p")
          # a = li2("a").attr.herf 空值？
          b = li2("h2")
          a = b("a") #<a></a> 标签中含有文字
          c = li2.remove("a") #移除a中已经打印的内容
          i += 1
          try:
                d = KKPrint(a.text(),c.text()[:-23],p.text()[-9:-4],p.text()[:-13],'','',a.attr.href) # 定义一d个类
                d.Page()
                sort.append(d.KKCout())
                print(sort)
          except:
                pass
      # json = json.dumps(sort, ensure_ascii=False)
      Save(sort, my_set)


# 爬取每一页的页码url,但是这个函数的迭代过程出不来，而且有重复的url（？不知道为甚）
def SortPage(url):
      mainurl = 'http://www.kekenet.com'
      # OnePage(url)
      r = requests.get(url)
      html = r.text
      r.encoding = 'utf-8'
      doc = pq(html)
      allpages = doc(".page").items()
      # 因为该页面的下一页会一直跳转，到最后一页也会跳转，不报错
      global sorturl
      j = 0
      for i in doc(".page a").items():
            if j == 7:
                  break
            if i not in sorturl:
                  print(j, i.attr.href)
                  sorturl.append(i.attr.href)
            j += 1
      while '/read/news/keji/List_1.shtml' not in sorturl:
            surl = mainurl + sorturl[-1]
            print(sorturl)
            print(len(sorturl))
            SortPage(surl)
      #       for i in sorturl[]
      #       ourl = mainurl + sorturl[0]
            # OnePage(ourl)
      # OnePage(sorturl[-1])


            
if __name__ == "__main__":
      url = 'http://www.kekenet.com/read/news/keji/'
      # SortPage(url)
      # 连接数据库
      conn = MongoClient('127.0.0.1', 27017)
      db = conn.keke
      my_set = db.test_set
      # print(sorturl)
      # 根据网页的url特点
      for i in range(1,259):
            purl = url+'List_'+str(i)+'.shtml'
            OnePage(purl,my_set)
            # try:
            #       purl = url+'List_'+str(i)+'.shtml'
            #       OnePage(purl)
            # except expression as identifier:
            #       pass
      


    