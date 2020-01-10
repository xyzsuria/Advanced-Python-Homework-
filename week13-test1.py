# 使用多进程的方法扩展上述程序，来对下载的文章进行文本抽取。
# 个人理解，使用多进程的方式进行下载文本
from pyquery import PyQuery as pq 
import requests
from multiprocessing import Queue 
from multiprocessing import Process
import os


def context(q,e,z):
      print('开始获取这个页面的中英内容了')
      while True:
            purl = q.get(True)
            r = requests.get(purl)
            r.encoding = 'utf-8'
            pagehtml = r.text
            # print(pagehtml)
            html = pq(pagehtml)
            article = html("#article")
            item = article.html() # 所有内容
            it = pq(item)
            # print(it)e
            en = it(".qh_en").text() # 英文内容全部以qh_en为标签属性
            e.put(en)
            zh = it(".qh_zg").text()
            z.put(zh)



def SaveEn(e):
      if 'entext' not in os.listdir():
            os.mkdir('entext')
      os.chdir(r'.\entext')
      i = 0
      while True:
            i += 1 
            text = e.get(True)
            saveall = open(str(i)+'en.txt','w',encoding='utf-8')
            saveall.write(text)

def SaveZh(z):
      if 'zhtext' not in os.listdir():
            os.mkdir('zhtext')
      os.chdir(r'.\zhtext')
      i = 0
      while True:
            i += 1
            text = z.get(True)
            saveall = open(str(i)+'zh.txt','w',encoding='utf-8')
            saveall.write(text)



def GetUrl(q, url):
      r = requests.get(url)
      mainurl = 'http://www.kekenet.com'
      r.encoding = 'utf-8' #解决乱码问题
      indexhtml = r.text
      # print(indexhtml)
      indexh = pq(indexhtml)
      lists2 = indexh("#menu-list li")
      for li in lists2.items():
            a = mainurl+li("a").attr.href
            q.put(a)



if __name__ == "__main__":
      url = 'http://www.kekenet.com/read/news/keji/'
      q = Queue()
      e = Queue()
      z = Queue()
      pg = Process(target=GetUrl, args=(q,url,))
      pq = Process(target=context, args=(q,e,z,))
      pe = Process(target=SaveEn, args=(e,))
      pz = Process(target=SaveZh, args=(z,))
      pg.start()
      pq.start()
      pe.start()
      pz.start()
      pq.join()
      pe.join()
      pz.join()
      pq.terminate()
      pe.terminate()
      pz.terminate()
