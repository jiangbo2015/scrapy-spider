# -*- coding: utf-8 -*-
import scrapy


from scrapy.spiders.crawl import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from ..items import DoubanbookItem

class DoubanSpider(CrawlSpider):
	name = "douban"
	allowed_domains = ["book.douban.com"]
	start_urls = ['https://book.douban.com/']

	rules = [
		Rule(LinkExtractor(allow=r'subject/\d+'),callback='parse_items')
	]

	def parse_items(self, response):
		items = DoubanbookItem()
		items['name'] = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract_first()
		items['author'] = response.xpath('//*[@id="info"]//a/text()').extract()
		yield items