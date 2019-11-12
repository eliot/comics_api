from peewee import CharField, TextField

from .base_model import ScrapeModel

class ComixologyStoryArc(ScrapeModel):
	class Meta:
		db_table = 'story_arc'
	name = CharField()
	description = TextField()
