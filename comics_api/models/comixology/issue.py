from peewee import CharField, IntegerField, TextField, FloatField, \
	ForeignKeyField, BooleanField, DateTimeField

from .base_model import ScrapeModel
from .publisher import ComixologyPublisher
from .volume import ComixologyVolume
from .series import ComixologySeries
from .story_arc import ComixologyStoryArc
from .ref_sold_by import ComixologyRefSoldBy
from .ref_age_rating import ComixologyRefAgeRating

class ComixologyIssue(ScrapeModel):
	'''An issue scraped from Comixology'''
	class Meta:
		db_table = 'issue'
	title = CharField() # title as it appears on Comixology e.g. Archie #1
	issue_id = IntegerField() # issue id from Comix
	description = TextField()
	price = FloatField()
	sold_by = ForeignKeyField(ComixologyRefSoldBy)
	age_rating = ForeignKeyField(ComixologyRefAgeRating)
	collected_edition = ForeignKeyField('self')
	is_collected_edition = BooleanField(default=False)
	issue_number_end = IntegerField()
	star_rating = IntegerField()
	ratings_count = IntegerField()
	
	# fields from base.Issue
	issue_number = IntegerField()
	print_release_date = DateTimeField()
	digital_release_date = DateTimeField()
	summary = TextField()
	cover_url = CharField()
	cover_price = FloatField()
	page_count = IntegerField()
	publisher = ForeignKeyField(ComixologyPublisher, backref='issues')
	volume = ForeignKeyField(ComixologyVolume, backref='issues')
	series = ForeignKeyField(ComixologySeries, backref='issues')
	storyarc = ForeignKeyField(ComixologyStoryArc, backref='issues')

