# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Request
import json


class DiscoverySpider(scrapy.Spider):
    name = 'discovery'
    allowed_domains = ['xinpianchang.com','https://openapi-vtom.vmovier.com']
    start_urls = ['https://www.xinpianchang.com/channel/index/id-0/sort-like/duration_type-0/resolution_type-/type-?from=articleListPage']

    def parse(self, response):
        pid_list = response.xpath(
            '//ul[@class="video-list"]/li/@data-articleid').extract()
        url = "https://www.xinpianchang.com/a%s?from=ArticleList"
        for pid in pid_list:

           yield response.follow(url %pid,self.parse_post)

    def parse_post(self,response):
        post={}
        post['title'] = response.xpath('//div[@class="title-wrap"]/h3/text()').get()
        # post['video'] = response.xpath()
        vid = re.findall('vid: \"(\w+)\"\,',response.text)
        video_url = 'https://openapi-vtom.vmovier.com/v3/video/%s?expand=resource&usage=xpc_web'
        cates = response.xpath('//span[contains(@class,"cate")]//text()').extract()
        post['category'] = ''.join([cate.strip() for cate in cates])
        post['create_at'] = response.xpath('//span[contains(@class,update-time)]/i/text()')
        request = Request(video_url % vid,callback=self.parse_video)
        request.meta['post'] = post
        yield request

    def parse_video(self,response):
        post = response.meta['post']
        result = json.loads(response.text)
        post['video'] = result['data']['resource']['default']['https_url']
        post['preview'] = result['data']['video']['cover']

        yield post






