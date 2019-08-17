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
	number = IntegerField() # e.g. Volume 1
	
class StoryArc(BaseModel):
	# e.g. Infinity War or Knightfall
	name = CharField()

class Playlist(BaseModel):
	'''User created lists of comics'''
	name = CharField()
	#owner = ForeignKeyField(User, backref='owner')

class Issue(BaseModel):
	issue_number = IntegerField()
	date_release_print = DateTimeField()
	date_release_digital = DateTimeField()
	publisher = ForeignKeyField(Publisher, backref='issues')
	volume = ForeignKeyField(Volume, backref='issues')
	series = ForeignKeyField(Series, backref='issues')
	summary = TextField()
	cover_url = CharField()
	cover_price = FloatField()

class PlayListItem(BaseModel):
	order = IntegerField()
	issue = ForeignKeyField(Issue)
	playlist = ForeignKeyField(Playlist, backref='items')

class Creator(BaseModel):
	'''A writer, drawer, or inker'''
	name = CharField()
	# role = Enum { Writer, Drawer/Pencils, Inker }

class Continuity(BaseModel):
	pass

class Universe(BaseModel):
	'''E.g. Marvel Cinematic Universe'''
	pass