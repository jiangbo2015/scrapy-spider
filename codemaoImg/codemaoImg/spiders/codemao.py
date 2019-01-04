# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import CodemaoimgItem

class CodemaoSpider(scrapy.Spider):
	name = 'codemao'
	allowed_domains = ['codemao.cn']
	total = 2898
	offset = 50
	url = "https://api.codemao.cn/web/materials?filter_type=CATEGORY&limit=10&offset="
	start_urls = [url+str(offset)]

	def parse(self, response):
		item = CodemaoimgItem()
		res = json.loads(response.text)
		item['data'] = res['items']
		yield item

		if self.offset < 999:
			self.offset += 100
			yield scrapy.Request(self.url+str(self.offset), callback=self.parse)

