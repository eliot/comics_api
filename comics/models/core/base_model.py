from peewee import Model

from ...config import db

class BaseModel(Model):
	class Meta:
		database = db
