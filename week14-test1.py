text = "在尼比鲁星球探查期间，企业号舰长柯克为营救史波克采取了胆大妄为的举动，几乎危及全舰队员的生命，他也为此付出代价。"

# snownlp
from snownlp import SnowNLP
doc = SnowNLP(text)
sans = doc.words
print(doc.words)

# jieba
import jieba
words = jieba.cut(text)
jans = [w for w in words] 
print(jans)


# stanfordcorenlp
# from stanfordcorenlp import StanfordCoreNLP
# nlp = StanfordCoreNLP('http://localhost',port=2002)
# print(nlp.word_tokenize(text))

# 正确的分词
ans = '在 尼比鲁星球 探查 期间 ，企业号 舰长 柯克 为 营救 史波克 采取 了 胆大妄为 的 举动 ， 几乎 危及 全舰 队员 的 生命 ， 他 也 为此 付出 代价 。'
rightans = list(map(str,ans.split()))# 获得分词列表
print(rightans)

# 如果列表中有同样的字符，num+1
def Count(a,b):
    c = a
    num = 0
    for i in b:
        if i in c:
            num += 1
            c.remove(i)
    # print(num)
    return num

# 比较两个列表长度
def Length(a,b):
    if len(a)>len(b):
        return Count(a,b)
    else:
        return Count(b,a)

# 输出函数，传入的ans是一个列表
def log(zh,ans):
    print("{}的准确率是：{:.2f}%".format(zh,ans[0]*100))
    print("{}的召唤率是：{:.2f}%".format(zh,ans[1]*100))
    print("{}的F-评价：{:.2f}%".format(zh,ans[2]*100))

# 进行计算（正确的字符数，切分总字符数，正确总字符数）
def JiSuan(trlen,tlen,rlen):
    a = []
    a.append(trlen/tlen)
    a.append(trlen/rlen)
    a.append(2*(a[0]*a[1])/(a[0]+a[1]))
    return a

# 主函数
jlen = len(jans)
slen = len(sans)
rlen = len(rightans)
jrlen = Length(jans,rightans)
srlen = Length(sans,rightans)
j = JiSuan(jrlen,jlen,rlen)
log("结巴分词",j)
s = JiSuan(srlen,slen,rlen)
log("snownlp",s)


