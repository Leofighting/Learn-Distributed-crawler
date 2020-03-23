# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['http://blog.jobbole.com']
    start_urls = ['http://http://blog.jobbole.com/']

    def parse(self, response):
        re_selector = response.xpath("/html/body/div[3]/div[2]/div[1]/h2")
        pass

