from peewee import CharField, IntegerField

from .base_model import ScrapeModel

class ComixologyGenre(ScrapeModel):
	class Meta:
		db_table = 'genre'
	name = CharField()
