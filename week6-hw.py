# books与 本文件在同一个文件夹下
import os
import re

def FindBook(name):
      try:
            x = open('books/'+name+'.txt', 'r')
            f = x.read()
                  # print(f)
            Save(f, name)
            x.close()
      except:
            print("输入的文件名不准确")

def Save(txt, name):
      nowpath = os.getcwd()
      try:
            os.mkdir(nowpath+'\Save')
      except:
            pass
      os.chdir(nowpath+'\Save') # 保存在Save文件夹下
      # print(os.getcwd())
      zech=re.compile(r'[\u4e00-\u9fa5,、,，“,”,。]')#匹配中文和标点
      zeen=re.compile(r'[\u0061-\u007a,\u0041-\u005a,\u0020,，,\',！,．]')#匹配英文
      en="".join(zeen.findall(txt))
      ch="".join(zech.findall(txt))
      wen=open(name+'en.txt','w')
      wch=open(name+'ch.txt','w')
      wen.write(en)#把英文写入创建的文本中
      wch.write(ch)
      wen.close()
      wch.close()
      os.chdir(nowpath)#再次切换原来文件所在的目录


if __name__ == "__main__":
      name = input("请输入要分中英文的文件名：")
      FindBook(name)
      # print(os.getcwd()) 当前路径
      # 用来测试的名字
      # 1A_06.猴爪
      # 1A_04.潘德尔的巫师

