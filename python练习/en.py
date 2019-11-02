#英文分句
import re
f=open('test.txt')
h=f.read()
#from nltk import sent_tokenize
#sent_tokenize(str1)
z=re.sub('[\n]+',' ',h)#将换行符替换成空格
h=z.replace('.','/')
y=h.replace('\'','#')
#print(y)
p=re.compile(r'[\w#\s,-."]{10,}[?!/]\s')
x=p.findall(y)
ans=[]
for l in x:
    x1=l.replace('/','.')
    x2=x1.replace('#','\'')
    ans.append(x2)
print(ans)
print(len(ans))
