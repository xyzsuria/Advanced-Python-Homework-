# 对于练习1抽取的文章数据，使用用nltk、stanfordcorenlp、
# spaCy分别进行练习使用其词法分析和句法分析相关功能。（可参考其官方文档）
import os
import nltk
from nltk.util import ngrams
import spacy

def UseNltk(txt):
    a = txt.split(' ') #进行英文切词
    for i in range(1,4):
        unigrams = ngrams(a,i)
        n = []
        for j in unigrams:
            n.append(j)
        print('ngram为{}的模型:{}'.format(i,n))
    
    

# def UseStandford():
# 这个模板用不了


def UseSpacy(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    # 分句
    list(doc.sents)
    # 词性标注
    for w in list(doc.sents)[0]:print(w,w.tag_)
    all_tags = {w.pos: w.pos_ for w in doc}
    # 命名实体检测
    print([ (w,w.label_)  for w in doc.ents])
    # 名词性短语
    print([np for np in doc.noun_chunks])


def Content(name):
    c = ''
    for i in os.listdir(name):
        f = open(name+'//'+i, 'r', encoding='utf-8')
        # 因为该文件夹中有很多.txt文件， 下面是把它们整合在一起
        text = f.read()
        c += text
    f.close()
    return c
        



if __name__ == "__main__":
    en = 'entext' # 抽出的英文文章所在的文件夹名
    zh = 'zhtext'
    c = Content(en)
    UseNltk(c)
    UseSpacy(c)
    # print(c)
    