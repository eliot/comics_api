from peewee import CharField

from .base_model import BaseModel

class Playlist(BaseModel):
	'''User created lists of comics'''
	name = CharField()
	#owner = ForeignKeyField(User, backref='playlists')
