from peewee import Model, CharField, DateTimeField, TextField
from datetime import datetime

# use a different database for each site scraped
from ...config import db_comixology 

class ScrapeModel(Model):
	'''An item scraped from Comixology'''
	class Meta:
		database = db_comixology
	date_scraped = DateTimeField(datetime.now, default=datetime.now)
	# url for the item scraped
	url = CharField(primary_key=True) 
	title = CharField()
	description = TextField()

class RefModel(Model):
	'''Barebones base model for reference tables'''
	class Meta:
		database = db_comixology
	
