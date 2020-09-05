# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DataExtractionItem(scrapy.Item):
    product_url = scrapy.Field()
    brand_name = scrapy.Field()
    product_name = scrapy.Field()
    item = scrapy.Field()
    price = scrapy.Field()
    size = scrapy.Field()
    
    # define the fields for your item here like:
    # name = scrapy.Field()
