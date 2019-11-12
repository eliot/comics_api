from peewee import IntegerField, ForeignKeyField

from .base_model import BaseModel

class PlayListItem(BaseModel):
	order = IntegerField()
	issue = ForeignKeyField(Issue)
	playlist = ForeignKeyField(Playlist, backref='items')
