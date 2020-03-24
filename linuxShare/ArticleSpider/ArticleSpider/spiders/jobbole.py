# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://www.jobbole.com/']

    def parse(self, response):

        # 解析列表页中的所有文章url并交给 scrapy 下载后，再进行解析
        post_urls = response.css("div.zhicheng_news_list a::attr(href)").extract()
        for post_url in post_urls:
            print(post_url)

        # 通过 xpath 提取字段
        title = response.xpath("//div[@class='ship_wrap']/h2/text()").extract()
        re_selector1 = response.xpath("//div[@class='meta']/span/text()").extract()
        content = response.xpath("//div[@class='wen_article']").extract()[0]

        # 通过 css 选择器 提取字段
        title_css = response.css(".ship_wrap h2::text").extract()

        pass
