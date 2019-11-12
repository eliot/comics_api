from peewee import CharField, IntegerField, TextField, FloatField, ForeignKeyField, DateTimeField

from .base_model import BaseModel
from .publisher import Publisher
from .volume import Volume
from .series import Series
from .story_arc import StoryArc

class Issue(BaseModel):
	issue_number = IntegerField()
	print_release_date = DateTimeField()
	digital_release_date = DateTimeField()
	summary = TextField()
	cover_url = CharField()
	cover_price = FloatField()
	page_count = IntegerField()
	publisher = ForeignKeyField(Publisher, backref='issues')
	volume = ForeignKeyField(Volume, backref='issues')
	series = ForeignKeyField(Series, backref='issues')
	storyarc = ForeignKeyField(StoryArc, backref='issues')
