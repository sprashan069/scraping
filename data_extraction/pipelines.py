# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import mysql.connector

class DataExtractionPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host= 'localhost',
            user = 'root',
            password = 'prashan1609',
            database = 'my_data'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS product""")
        self.curr.execute("""create table product(
                        product_url text,
                        brand_name text,
                        product_name text,
                        item text,
                        price text,
                        size text

                        )""")



    def process_item(self, item, spider):
        self.store_db(item)
        return item


    def store_db(self,item):
        self.curr.execute("""insert into product values (%s, %s, %s, %s, %s, %s)""",(
            item['product_url'],
            item['brand_name'],
            item['product_name'],
            item['item'],
            item['price'],
            item['size']
        ))
        self.conn.commit()
    
    # def process_item(self, item, spider):
    #     return item
