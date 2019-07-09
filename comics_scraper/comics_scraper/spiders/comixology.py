# -*- coding: utf-8 -*-
import scrapy


class ComixologySpider(scrapy.Spider):
    name = 'comixology'
    allowed_domains = ['comixology.com']
    start_urls = ['http://comixology.com/']

    def parse(self, response):
        pass
