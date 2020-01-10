# 计算上述例子中段落的词性分布
import spacy
def UseSpacy():
    nlp = spacy.load('en_core_web_sm')
    text="2019 is coming to a close, and with it, we've seen some interesting trends that come and go in the health and wellness industry. This is a constantly evolving area where areas of interest come and go with new trends appearing as new technology and information are made accessible to the broader public. In 2019, we saw an interesting shift toward new therapies, including an increase in CBD-based products, as well as a continued rise in the number of apps and technology to improve well-being and health."
    doc = nlp(text)
    # 分句
    list(doc.sents)
    # 词性标注
    for w in list(doc.sents)[0]:print(w,w.tag_)
    all_tags = {w.pos: w.pos_ for w in doc}
    # 命名实体检测
    name = [ (w,w.label_)  for w in doc.ents]
    # 名词性短语
    n = [np for np in doc.noun_chunks]
    Coculate(name)

def Coculate(nlist):
    x = []
    y = {} #记录词性出现的次数
    # 设置一个空的列表，记录出现过的词性
    # print(nlist)
    for i in nlist:
        if i[1] not in x:
            x.append(i[1])
            y[i[1]] = 1
        else:
            y[i[1]] += 1
    print(y)


if __name__ == "__main__":
    UseSpacy()