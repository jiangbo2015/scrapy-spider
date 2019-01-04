# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request


class CodemaoimgPipeline(object):
	def process_item(self, item, spider):
		return item

# 只能下载图片
class CodemaoimgImgPipeline(ImagesPipeline):
	def file_path(self, request, response=None, info=None):
		name = request.meta['name']
		ext = request.meta['type']
		if ext not in ['png', 'gif', 'jpg', 'jpeg']:
			filename = u'full/{0}'.format(name)
			return filename

	def get_media_requests(self, item, spider):
		for x in item['data']:
			image_url = x['resource_urls'][0]
			ext = image_url.split('/')[-1].split('.')[-1]
			name = x["name"] + '.' + ext 
			yield Request(image_url, meta={"name": name, "type": ext})

	def item_completed(self, results, item, info):
		return item

# 可以同时下载图片文件

class CodemaoimgFilePipeline(FilesPipeline):

	def file_path(self, request, response=None, info=None):
		name = request.meta['name']
		ext = request.meta['type']
		filename = u'full/{0}'.format(name)
		return filename

	def get_media_requests(self, item, spider):
		for x in item['data']:
			image_url = x['resource_urls'][0]
			ext = image_url.split('/')[-1].split('.')[-1]
			name = x["name"] + '.' + ext 
			yield Request(image_url, meta={"name": name, "type": ext})
