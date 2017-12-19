# -*- coding: utf-8 -*-
import scrapy


class MydomainSpider(scrapy.Spider):
    name = 'mydomain'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
