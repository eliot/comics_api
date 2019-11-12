from peewee import CharField

from .base_model import ScrapeModel

class ComixologyPublisher(ScrapeModel):
	class Meta:
		db_table = 'publisher'
	name = CharField()
