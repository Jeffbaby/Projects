# -*- coding:utf-8 -*-
#!python3
import re
path = 'test.txt'
with open(path, 'r', encoding='utf-8') as f:
  word_list = []
  word_reg = re.compile(r'\w+')
  for line in f:
    #line_words = word_reg.findall(line)
    #比上面的正则更加简单
    line_words = line.split()
    word_list.extend(line_words)
  word_set = set(word_list) # 避免重复查询
  words_dict = {word: word_list.count(word) for word in word_set}
  for k, v in words_dict.items():
    print(k, v)