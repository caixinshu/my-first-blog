# -*- coding: utf-8 -*-
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def __init__(self,mysql_uri,mysql_db,*args,**kwargs):
        super(ZhihuSpider, self).__init__(*args,**kwargs)
        self.mysql_uri = mysql_uri
        self.mysql_db = mysql_db


    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mysql_uri = crawler.settings.get('MONGO_URI'),
            mysql_db = crawler.settings.get('MONGO_DB')
        )

    def parse(self, response):
        self.logger.info(response.status)

