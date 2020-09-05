import scrapy
from data_extraction.items import DataExtractionItem

class DataExractSpider(scrapy.Spider):
    name = 'data'
    # the start_urls list is extracting the html page 
    start_urls = ['https://www.ulta.com/thank-u-next-eau-de-parfum?productId=pimprod2008597']

    # this custom setting is for csv file to store scrape data.  
    '''custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'data.csv'
    }'''

    # this function is parsing the reponse and scrape the data
    def parse(self, response):

        ''' This it the item object which passing the scrape data 
        to pipeline.py file to store the items in mysql database table'''

        items = DataExtractionItem()
        for product in response.css('section.ProductDetail__content'):
            
            items['product_url']= product.xpath('//*[@id="js-mobileBody"]/div/div/div/div/div/div/section[1]/div[2]/div/h1/div[1]/a/@href').get()
            items['brand_name']= product.xpath('//*[@id="js-mobileBody"]/div/div/div/div/div/div/section[1]/div[2]/div/h1/div[1]/a/p/text()').get()
            items['product_name']= product.xpath('//*[@id="js-mobileBody"]/div/div/div/div/div/div/section[1]/div[2]/div/h1/div[2]/span/text()').get()
            items['item']=product.xpath('//*[@id="js-mobileBody"]/div/div/div/div/div/div/section[1]/div[2]/div/div[1]/p/text()').get()
            items['price']= product.xpath('//*[@id="js-mobileBody"]/div/div/div/div/div/div/section[1]/div[2]/div/div[3]/span/text()').get()
            items['size']= product.xpath('//*[@id="js-mobileBody"]/div/div/div/div/div/div/section[1]/div[3]/div/div[1]/div[2]/span[2]/text()').get()
        yield items

        change_size = response.xpath('//*[@id="js-mobileBody"]/div/div/div/div/div/div/section[1]/div[3]/div/div[2]/ul/div[2]/div/div/div[2]').get()
        print('~~~> size',change_size)
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
