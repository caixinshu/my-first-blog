# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#
# class QuotePipeline(object):
#     def process_item(self, item, spider):
#         return item
import pymysql
from scrapy.exceptions import DropItem
class TextPipeline(object):

    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        if item['text']:
            if len(item['text']) > self.limit:
                item['text'] = item['text'][0:self.limit].rstrip()+'...'
            return item
        else:
            return DropItem

class MysqlPipeline(object):

    def open_spider(self,spider):
        self.conn = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            db = 'quotes_04',
            user = 'root',
            password = 'root',
            charset = 'utf8',
        )
        self.cur = self.conn.cursor()

    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()

    def process_item(self,item,spider):
        # keys = item.keys()
        # values = list(item.values())
        keys,values = zip(*item.items())
        sql = 'insert into quotes ({}) values ({})'.format(
            ','.join(keys),','.join(['%s'] * len(values))
        )
        self.cur.execute(sql,values)
        self.conn.commit()
        print(self.cur._last_executed)
        return item



# class MOngoPipeline(object):
#
#     def __init__(self,mongo_url,mongo_db):
#         self.mongo_uri = mongo_url
#         self.mongo_db = mongo_db
#
#     @classmethod
#     def from_crawler(cls,crawler):
#         return cls(
#             mongo_uri = crawler.settings.get('MONGO_URI'),
#             mongo_db = crawler.settings.get('MONGO_DB')
#         )
#
#     def open_spoder(self,spider):
#         self.client = pymongo.MongoClient(self.mongo_uri)
#         self.db = self.client[self.mongo_db]
#
#     def process_item(self, item, spider):
#         name = item.__class__.__name__
#         self.db[name].insert(dict(item))
#         return item
    

























