import os
from peewee import *
from config import DB_URI

db = SqliteDatabase(DB_URI)

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
	# user curated lists of comics
	name = CharField()

class Issue(BaseModel):
	number = IntegerField()
	published = DateTimeField()
	publisher = ForeignKeyField(Publisher, backref='issues')
	volume = ForeignKeyField(Volume, backref='issues')
	series = ForeignKeyField(Series, backref='issues')
	summary = TextField()
	cover_url = CharField()

class CreativePerson(BaseModel):
	'''A person who wrote, drew, or inked an issue'''
	name = CharField()
	# role = Enum { Writer, Drawer, Inker }

# Continuity
class Continuity(BaseModel):
	pass

# Universe
class Universe(BaseModel):
	pass