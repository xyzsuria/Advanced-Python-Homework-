# 文本处理
import spacy

def UseSpacy(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    # 分句
    list(doc.sents)
    # 词性标注
    for w in list(doc.sents)[0]:print(w,w.tag_)
    all_tags = {w.pos: w.pos_ for w in doc}
    # 命名实体检测
    n = [ (w,w.label_)  for w in doc.ents]
    Coculate(n)


def Coculate(nlist):
    x = []
    y = {} #记录词性出现的次数
    # 设置一个空的列表，记录出现过的词性
    for i in nlist:
        if i[1] not in x:
            x.append(i[1])
            y[i[1]] = 1
        else:
            y[i[1]] += 1
    print(y)

def Txt(name):
    try:
        f = open(name, 'r', encoding='utf-8')
        text = f.read()
        f.close()
        return text
    except:
        print("文件名可能不正确")

if __name__ == "__main__":
    name = input("请输入正确的文件路径名")
    try:
        n = Txt(name)
        UseSpacy(n)
    except:
        pass


