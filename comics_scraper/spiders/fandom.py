# -*- coding: utf-8 -*-
import scrapy

class FandomSpider(scrapy.Spider):
    name = 'fandom'
    allowed_domains = ['dc.fandom.com', ]
    start_urls = ['http://fandom.com/']
    rules = None

    def parse(self, response):
        pass
