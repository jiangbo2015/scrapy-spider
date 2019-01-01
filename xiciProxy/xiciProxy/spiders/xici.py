# -*- coding: utf-8 -*-
import scrapy
from ..items import XiciproxyItem
import requests

class XiciSpider(scrapy.Spider):
	name = 'xici'
	allowed_domains = ['xicidaili.com']
	start_urls = ['https://www.xicidaili.com/nn/1']

	def parse(self, response):

		for each in response.xpath('//tr[position() > 1]'):
			item = XiciproxyItem()
			ip = each.xpath('./td[2]/text()').extract()[0]
			port = each.xpath('./td[3]/text()').extract()[0]
			type = each.xpath('./td[6]/text()').extract()[0]
			proxies = {
				type: str(ip)+str(port)
			}
			try:
				r = requests.get('https://www.baidu.com', proxies=proxies, timeout=2)
				print(r.status_code)
				item['ip'] = ip
				item['port'] = port
				item['type'] = type
				yield item

			except:
				print('pass'+str(proxies))
