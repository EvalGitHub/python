# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#引入codecs打开文件，可以避免很多，编码问题
import codecs
import json

from scrapy.pipelines.images import  ImagesPipeline

import MySQLdb
import MySQLdb.cursors

from twisted.enterprise import adbapi

class ArticlespliderPipeline(object):
    def process_item(self, item, spider):
        return item


#存放数据库(方式一)
class MysqlPipeline(object):
    def __init__(self):
        #链接
        # self.conn= MySQLdb.connect('host','user','password','dbname',charset="utf8",user_unicode=True)
        self.conn = MySQLdb.connect(host='127.0.0.1', user="root",db='article_spider', charset="utf8", use_unicode=True)
        #游标
        self.cursor=self.conn.cursor()
        #重载process_item
    def process_item(self,item,spider):
        insert_sql="""insert into article(title,url,create_date,fav_nums) VALUES (%s,%s,%s,%s)"""
        self.cursor.execute(insert_sql, (item['title'], item['url'], item['create_date'], item['fav_nums']))
        # insert_sql = """select * from article"""
        #self.cursor.execute(insert_sql)
        self.conn.commit()

#使用twisted将同步操作变成异部（方式二）
class MysqlTwistedPipline(object):
    def __init__(self,dbpool):
        self.dbpool=dbpool

    @classmethod
    def from_settings(cls,settings):#这个settings就是我们的setting文件夹，可以取到我们所需要的内容
        dbparms =dict(
            host=settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd = settings["MYSQL_PASSWORD"],
            cursorclass=MySQLdb.cursors.DictCursor,
            charset="utf8",
            use_unicode=True)

        dbpool= adbapi.ConnectionPool("MySQLdb",**dbparms)
        return cls(dbpool)

    def process_item(self,item,spider):
       #使用twisted将mysql插入变成异步执行
        query=self.dbpool.runInteraction(self.do_insert,item)
        query.addErrback(self.handel_error)#处理异常

    def handel_error(self,failure):
        #处理异步插如异常
        print(failure)



    def do_insert(self,cursor,item):
        insert_sql = """insert into article(title,url,create_date,fav_nums) VALUES (%s,%s,%s,%s)"""
        cursor.execute(insert_sql, (item['title'], item['url'], item['create_date'], item['fav_nums']))
        # insert_sql = """select * from article"""



#存放数据
class JsonWidthEncodingPipeline(object):
    def __init__(self):
        self.file =codecs.open("article.json","w",encoding="utf-8")
    def process_item(self,item,spider):
        lines=json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(lines)
        return item

    def spider_closed(self,spider):
        self.file.close()


#下载图片
class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self,results,item,info):
        for ok, value in results:
            image_file_path=value['path']
        item['font_image_path']=image_file_path
        return item


