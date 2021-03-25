from peewee import CharField

from .base_model import BaseModel

class StoryArc(BaseModel):
	# e.g. Infinity War or Knightfall
	name = CharField()
