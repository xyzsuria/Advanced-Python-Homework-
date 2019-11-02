#高级的英文分句，除了要下载nltk
import re
f=open('test.txt')
h=f.read()
from nltk import sent_tokenize
str1=sent_tokenize(h)
print(str1)