# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#引入codecs打开文件，可以避免很多，编码问题
import codecs
import json

from scrapy.pipelines.images import  ImagesPipeline

class ArticlespliderPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWidthEncodingPipeline(object):
    def __init__(self):
        self.file =codecs.open("article.json","w",encoding="utf-8")
    def process_item(self,item,spider):
        lines=json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(lines)
        return item

    def spider_closed(self,spider):
        self.file.close()

class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self,results,item,info):
        for ok, value in results:
            image_file_path=value['path']
        item['font_image_path']=image_file_path
        return item


