题目：文本特征抽取：参考Coh-Metrix version3.0 indices，编写自己的mini版Coh-Metrix（中文或英文），只需要实现 Descriptive、Lexical Diversity 和Readability 中的指标，每类指标至少选取三个以上指标进行实现。 输出结果可以参考Cohmatrix-Webtool。验证方法，找任意文章作为输入，输出实现的各指标的数值结果。


步骤：
明确描述性(Descriptive)、可读性(Readalility)的指标和考察内容
* 描述性(Descriptive)

指标 | 命名|
:--:|:-:|
|段落数|ParagraphNum|
|句子数|SentenceNumber|
|单词数|WordNumber|
|平均句子长度|meansw|
|平均段落长度标准方差|使用函数返回值|
|平均句子单词数|dessl|
|单词(zh词汇)的平均长度|wmeanlength|
|单词平均长度标准方差|deswlit|


* 可读性(Readalility)

1. The output of the Flesch Reading Ease formula is a number from 0 to 100, with a higher score indicating easier reading.

 命名|计算函数
:-:|:----:
|RDFRE|READFRE = 206.835 - (1.015 x ASL) - (84.6 x ASW)|
ASL = average sentence length = the number of words divided by the number of sentences.
ASW (comes from CELEX database) = average number of syllables per word（每个词组的平均汉字数）

主要操作：
* 中英文切分句子
* 中英文切词
* 统计每个段落中存在多少句子，每个句子中存在多少单词
* 细微处理
1. 统计单词数，把标点符号去除
2. 把一些换行符替换掉

亮点：
* 模块化
* 使用判别语种的函数 `langid.classify()`
* 计算函数模块化

缺点：
* 部分指标省去
* 使用打开txt文件读入数据的方法，仍有缺陷
* 命名没有做到统一化

