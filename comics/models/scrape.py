from datetime import datetime

from peewee import Model, CharField, ForeignKeyField, DateTimeField
from playhouse.postgres_ext import JSONField

from comics.config import db

'''Generic models used for storing raw scraped data in Postgres.'''

class BaseModel(Model):
	class Meta:
		database = db

class ScrapeSite(BaseModel):
    '''Reference table for websites we scrape from. E.g. Comixology.com, Wikipedia'''
    #scrape_site_id = AutoField(primary_key=True)
    name = CharField()

class ScrapeItem(BaseModel):
    '''Metadata for a scraped page.'''
    #scrape_item_id = AutoField(primary_key=True)
    # scrape_site_id = SmallIntegerField() # FK to ScrapeSite.scrape_site_id
    site = ForeignKeyField(ScrapeSite, backref='items')
    url = CharField()
    date_scraped = DateTimeField(default=datetime.now)

class ScrapeData(BaseModel):
    '''JSON data for a scraped page.'''
    item = ForeignKeyField(ScrapeItem, backref='data')
    data = JSONField()
