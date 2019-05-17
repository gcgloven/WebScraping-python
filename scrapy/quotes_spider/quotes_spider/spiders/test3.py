# -*- coding: utf-8 -*-
import scrapy


class Test3Spider(scrapy.Spider):
    name = 'test3'
    allowed_domains = ['www.ourhousepropertymanagement.com/faq']
    start_urls = ['http://www.ourhousepropertymanagement.com/faq/']

    def parse(self, response):
        pass
