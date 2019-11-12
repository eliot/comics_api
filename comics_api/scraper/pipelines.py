from ..models.comixology import *

class PeeweePipeline(object):
    '''Save to DB using Peewee'''

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
