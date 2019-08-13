import os
from peewee import *
from config import db

class BaseModel(Model):
	class Meta:
		database = db

class Publisher(BaseModel):
	name = CharField()

class Series(BaseModel):
	# sequence of issues with the same title e.g. Detective Comics
	# e.g. Batman
	title = CharField()
	summary = TextField()

class Volume(BaseModel):
	# start and end year
	# a collection of issues
	# - run of the comics, e.g. 3 volumes of Batman
	name = CharField()
	
class StoryArc(BaseModel):
	# e.g. Infinity War or Knightfall
	name = CharField()

class Playlist(BaseModel):
	'''User created lists of comics'''
	name = CharField()
	#owner = ForeignKeyField(User, backref='owner')


class Issue(BaseModel):
	number = IntegerField()
	published = DateTimeField()
	publisher = ForeignKeyField(Publisher, backref='issues')
	volume = ForeignKeyField(Volume, backref='issues')
	series = ForeignKeyField(Series, backref='issues')
	summary = TextField()
	cover_url = CharField()

class PlayListItem(BaseModel):
	order = IntegerField()
	issue = ForeignKeyField(Issue)
	playlist = ForeignKeyField(Playlist, backref='items')

class ComixologyIssue(Issue):
	'''Table to hold issues scraped serially from Comixology URLs'''
	class Meta:
		db_table = 'issue_comixology'
	url = TextField()
	issue_id = IntegerField()
	date_scraped = DateTimeField()

class CreativePerson(BaseModel):
	'''A person who wrote, drew, or inked an issue'''
	name = CharField()
	# role = Enum { Writer, Drawer, Inker }

# Continuity
class Continuity(BaseModel):
	pass

# Universe
class Universe(BaseModel):
	'''E.g. Marvel Cinematic Universe'''
	pass