# -*- coding: utf-8 -*-
import scrapy
from ..items import Music163Item

class MusicSpider(scrapy.Spider):
	name = 'music'
	allowed_domains = ['music.163.com']
	offset = 0
	url = "https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset="
	start_urls = [url+str(offset)]


	def parse(self, response):
		for each in response.xpath('//ul[@id="m-pl-container"]/li'):
			item = Music163Item()
			item['name'] = each.xpath('.//a[@class="msk"]/@title').extract()[0]
			item["playNums"] = each.xpath('.//span[@class="nb"]/text()').extract()[0]
			yield item

		if self.offset < 1260:
			self.offset += 35
			yield scrapy.Request(self.url+str(self.offset), callback=self.parse, dont_filter=True)

