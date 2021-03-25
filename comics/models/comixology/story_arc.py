from peewee import CharField, TextField, IntegerField

from .base import BaseModel

class ComixologyStoryArc(BaseModel):
	class Meta:
		db_table = 'comixology_story_arc'
	name = CharField()
	description = TextField()
	storyarc_id = IntegerField(primary_key=True)
