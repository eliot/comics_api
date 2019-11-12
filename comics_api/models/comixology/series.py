from peewee import CharField, TextField

from .base_model import ScrapeModel

class ComixologySeries(ScrapeModel):
	class Meta:
		db_table = 'series'
