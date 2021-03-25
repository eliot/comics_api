from peewee import CharField, IntegerField, TextField, FloatField, \
	ForeignKeyField, BooleanField, DateTimeField

from .base import BaseModel
from .publisher import ComixologyPublisher
from .volume import ComixologyVolume
from .series import ComixologySeries
from .story_arc import ComixologyStoryArc
from .ref_sold_by import ComixologyRefSoldBy
from .ref_age_rating import ComixologyRefAgeRating

class ComixologyIssue(BaseModel):
	'''An issue scraped from Comixology'''
	class Meta:
		db_table = 'comixology_issue'
	title = CharField() # title as it appears on Comixology e.g. Archie #1
	issue_id = IntegerField(primary_key=True) # issue id from Comixology.com
	description = TextField()
	price = FloatField()
	sold_by = ForeignKeyField(ComixologyRefSoldBy)
	age_rating = ForeignKeyField(ComixologyRefAgeRating)
	# points to the collected edition that contains this issue
	collected_edition = ForeignKeyField('self')
	# if this issue is a collected edition (other issues point to it)
	# (possibly to be marked later by sql job)
	is_collected_edition = BooleanField(default=False)
	# if this "issue" is two or more issues combined into one e.g. #11-12
	# null if it is a normal issue (most of the time)
	issue_number_end = IntegerField()
	# star rating system from Comixology.com
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

	is_volume = BooleanField()
	# "full price" or "original price" (price before fake discount)
	# e.g. https://www.comixology.com/Goodnight-Batcave/digital-comic/429218

	publisher = ForeignKeyField(ComixologyPublisher, backref='issues')
	# volume = ForeignKeyField(ComixologyVolume, backref='issues')
	series = ForeignKeyField(ComixologySeries, backref='issues')
	storyarc = ForeignKeyField(ComixologyStoryArc, backref='issues')
