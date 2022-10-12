# -*- coding : utf-8 -*-
# @Time      : 2022-04-07 16:06
# @Author    : Zong
# @File      : jieba.py
# @Software  : PyCharm
# @Function  : 
# @ChangeLog :

import News

import jieba
import jieba.analyse

jieba.initialize()  # 手动初始化（可选）

# 生成组合句
sentence = ""
for top_headline in News.top_headlines['articles']:
    sentence = top_headline['title']  + "。" + sentence


result = jieba.analyse.extract_tags(sentence, topK=20, withWeight=True, allowPOS=())
print(result)