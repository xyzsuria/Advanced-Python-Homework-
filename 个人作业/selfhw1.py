import nltk
import langid # 用来识别语种的函数
import re
import jieba
# 用来计算列表中句子数和单词总数的函数
def MeanLength(li):
    num = [len(i) for i in li]
    meanlength = sum(num)/len(num)
    return meanlength

# 计算段落数
def Despc(a):
    ParagraphNumber = a.count('\n')
    return ParagraphNumber

def RemoveBiaoDian(type,sentence):
    zhbiaodian = ['——','。','？','，','<','>','、','！','……','“','”','：']
    enbiaodian = [',','.','?','!','\\','《','》',':',';','"','"']
    if type == 'zh':
        w = list(jieba.cut(sentence, cut_all=True))
        sword = list(filter(None, w))
        for i in zhbiaodian:
            if i in sword:
                sword.remove(i)
        return sword
    elif type == 'en':
        w = nltk.word_tokenize(sentence)
        sword = list(filter(None, w))
        for i in enbiaodian:
            if i in sword:
                sword.remove(i)
        return sword
    else:
        print("输入有误。")
        return 0

# 计算句子总数和单词总数
def Dessc(a):
    langtype = {'en':'english','fr':'french','de':'german'}
    lang = langid.classify(a)
    # 如果识别的语种是中文
    if lang[0] == "zh":
        # 把空格和换行符都给替换掉
        x = re.sub('[\r\n\t\s]','',a)
        y = re.split(r'[。！？“”]', x)
        # 去除列表中可能出现的空格
        sentence = list(filter(None, y))
        # 计算每个处理过的句子列表中词汇
        senword = []
        for i in sentence:
            # 去除列表中的标点符号
            sword = RemoveBiaoDian('zh',i)
            senword.append(len(sword))
        # 平均句子长度（句子单词数）
        meansw = sum(senword)/len(senword)

        # 计算列表中句子数
        SentenceNumber = len(sentence)
        # 切词，去除标点, 返回单词列表
        word = RemoveBiaoDian('zh',a)
        tagged = nltk.pos_tag(word)
        # 每个单词长度的列表
        wlength = [len(j) for j in word]
        # 计算单词总数
        WordNumber = len(word)
        wmeanlength = sum(wlength)/WordNumber
        # 标准方差
        # 平均句子单词数标准方差
        dessl = FangCha(sword,meansw)
        # 单词平均长度标准方差
        deswlit = FangCha(word,wmeanlength)
       
        
        return [SentenceNumber,WordNumber, meansw, wmeanlength, dessl,deswlit]
    
    elif lang[0] in list(langtype.keys()):
        sentence = nltk.sent_tokenize(a, langtype[x[0]])
        SentenceNumber = len(sentence)
        word = RemoveBiaoDian('en', a)
        wlength = [len(j) for j in word]
        WordNumber = len(word)
        wmeanlength = sum(wlength)/WordNumber
        senword = []
        for i in sentence:
            sword = RemoveBiaoDian('en', i)
            senword.append(len(sword))
        meansw = sum(senword)/len(senword)

        return [SentenceNumber,WordNumber, meansw, wmeanlength, dessl,deswlit]


    else: 
        print("无法识别此语种。")
   
# 计算单词的总数
def deswc(a):
    a = nltk.word_tokenize(a)


# 计算标准方差 
# FangCha(列表，平均数)   
def FangCha(li,meannum):
    num = [(len(i)-meannum)*(len(i)-meannum) for i in li]
    result = pow(sum(num)/len(num), 0.5)
    return result

# 计算可读性，可读性=206.835-（1.015*平均句子长度 asl）-（84.6*每个词组中的平均汉字数 asw）
def Refre(asl, asw):
    readabilty = 206.835 - (1.015*asl)-(84.6*asw)
    return readabilty

# 计算段落长度的标准方差
def MeanParagraphLength(a, meanlength):
    ParagraphNum = Despc(a)
    Paragraph = re.split('\n',a)
    length = []
    try:
        for i in Paragraph:
            x = Dessc(i)
            length.append(x[0])
        num = [(j-meanlength)*(j-meanlength) for j in length]
        result = pow(sum(num)/len(num), 0.5)
        return result
    except:
        pass
     
# y = '武汉一定能度过难关。\n加油！\n我相信疫情一定会得到控制。'
fi = open('x.txt', 'r', encoding='utf-8')
y = fi.read()
print(type(y))
fi.close()
# 计算段落数
ParagraphNum = Despc(y) + 1
print("段落数是：",ParagraphNum)
x = Dessc(y)
# 平均段落长度
MeanLength = x[0]/ParagraphNum
print("平均段落长度：", MeanLength)
# 平均段落长度标准方差
print("平均段落长度标准方差：", MeanParagraphLength(y, MeanLength))
print("[句子数, 单词数, 平均句子长度，平均单词长度，平均句子单词数长度，单词平均长度标准方差]",x)

print("句子可读性：",Refre(x[2],x[3]))

