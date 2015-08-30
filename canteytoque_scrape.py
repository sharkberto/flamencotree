import scrapy
from scrapy.exceptions import DropItem
from scrapy.contrib.exporter import JsonItemExporter
import json

class TestItem(scrapy.Item):
	id = scrapy.Field()
	name = scrapy.Field()
	description = scrapy.Field()

	
class MySpider(scrapy.Spider):
	name = 'http://canteytoque.es/letrastodas.htm'
	allowed_domains = ['http://canteytoque.es/']
	start_urls = ['http://canteytoque.es/letrasmagujetajondo.html']

	
def parse(self, response):
        f = open('rawtitleletras','w+')
        for sel in response.xpath('/html/body'):
            f.write(str(response.xpath('/html/body/p' + ).extract()))
            f.write(str(response.xpath('/html/body/p/text()').extract()))
        f.close()

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.jl', 'wb')

        
    def process_item(self, item, MySpider):
        if item['title']:
            if item['desc']:
                line = json.dumps(dict(item)) + "\n"
                self.file.write(line)
                return item
            else:
                raise DropItem("Missing body or title of song in %s" % item)
