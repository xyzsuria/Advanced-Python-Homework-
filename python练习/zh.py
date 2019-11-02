import re
fil=open('y2test.txt',encoding='utf-8')#打开的文件名为y2.text.txt,与xtry.py在同一个目录下
para1=fil.read()
#print(para)
para2=re.sub('[。”]{2}','#',para1)#把中文中的。”替换成#
para3=re.sub('[？”]{2}','}',para2)
para=re.sub('[,”]{2}','{',para3)
sen=re.split('(#|}|{|。|！|!|？)',para)#根据标点符号进行切割
fil.close()
#sen=re.findall(u'[\u4e00-\u9fa5].+?',sen1[0])这里的正则表达式只能匹配中文
print(sen)
new_sen=[]
ans=[]
for i in range(int(len(sen)/2)):
    sent=sen[2*i]+sen[2*i+1]
    #print(sent)
    new_sen.append(sent)
if len(sen)%2==1:
    new_sen.append(sen[-1])
print(sen[-1])
for x in new_sen:
    a=x.replace('\n\u3000\u3000','')
    b=a.replace('#','。”')
    c=b.replace('}','？”')
    y=c.replace('{','，”')
    ans.append(y)
    print(y)
print(ans)