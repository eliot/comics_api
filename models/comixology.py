from general import Issue

class ComixologyIssue(Issue):
	'''An issue scraped from Comixology'''
	class Meta:
		db_table = 'issue_comixology'
	url = TextField()
	title = CharField() # title as it appears on Comixology e.g. Archie #1
	issue_id = IntegerField(primary_key=True)
	description = TextField()
	date_scraped = DateTimeField()
	price = FloatField()
	page_count = IntegerField()
	sold_by = ForeignKeyField(ComixologySoldBy, backref='seller')
	collected_edition = ForeignKeyField(ComixologyIssue)
	is_collected_edition = BooleanField(default=False)

class ComixologySeries(BaseModel):
	name = CharField()
	url = CharField()

class ComixologyStoryArc(BaseModel):
	name = CharField()
	url = CharField()

class ComixologyCreator(BaseModel):
	name = CharField()
	url = CharField()

class ComixologyPublisher(BaseModel):
	name = CharField()
	url = CharField()

class ComixologyGenre(BaseModel):
	class Meta:
		db_table = 'ref_comixology_genre'
	genre = CharField()

class ComixologySoldBy(BaseModel):
	class Meta:
		db_table = 'ref_comixology_soldby'
	seller_name = CharField()

class ComixologyAgeRating(BaseModel):
	class Meta:
		db_table = 'ref_comixology_agerating'
	age_rating = CharField()
	
class ComixologySoldBy(BaseModel):
	class Meta:
		db_table = 'ref_comixology_soldby'
	seller_name = CharField()

class ComixologyCreativeRole(BaseModel):
	class Meta:
		db_table = 'ref_comixology_creativerole'


class ComixologyCredit(BaseModel):
	'''Represents a credit to a creative Creator on a particular issue. 
	E.g. Joe Smith was the 1st (listed first) writer for "Donkey Demons #1"'''
	order = IntegerField()
	issue = ForeignKeyField(ComixologyIssue)
	Creator = ForeignKeyField(ComixologyCreator)
	role = ForeignKeyField(ComixologyCreativeRole)