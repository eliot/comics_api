from ..models.comixology import *

class PeeweePipeline(object):
    '''Save to DB using Peewee'''
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            db=crawler.settings.get('MONGO_URI')
        )

	# setup 
    def open_spider(self, spider):
        # get database from spider
        self.db = db

	# cleanup
    def close_spider(self, spider):
        self.client.close()

	# the primary work-doing callback
    def process_item(self, item, spider):
		item.save()
        return item
