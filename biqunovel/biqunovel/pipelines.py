# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import os
import json

#生成文本格式
class BiqunovelPipeline(object):
    def process_item(self, item, spider):
        #base_dir = os.getcwd()
        filename = 'jueshizhanshen.txt'
        with open(filename, 'a+') as f:
            f.write(item['title'].strip() + '\n')
            '''
            for line in item['content']:
                line = line.strip()  #去掉文本前后空格
                f.write(line)
            f.write(item['content'].strip())
            '''
            f.write(item['content'])
            f.write('\n\n')
        return item


#生成json格式
'''
class JsonPipeline(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + '/novel.json'
        with codecs.open(filename, 'a') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)
        return item
'''


