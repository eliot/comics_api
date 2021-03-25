import copy
from scrapy import Item, Field

# from ..models.comixology import *
'''
class GenericItem(Item):
	date_scraped = DateTimeField(datetime.now, default=datetime.now)
	url = CharField(primary_key=True)
	title = CharField() # page title, not necessarily a comic title
	description = TextField() # page description
'''
class IssueItem(Item):
	# metadata fields
	scrape_site = Field()
	url = Field()
	type = Field()

	# regular fields
	issue_id = Field(serializer=int)
	title = Field()
	issue_number = Field(serializer=int)
	issue_number_end = Field(serializer=int)
	is_multi_issue = Field()
	series = Field()
	series_url = Field()
	price = Field()
	cover_url = Field()
	description = Field()
	publisher = Field()
	publisher_url = Field()
	writers = Field()
	# writers_urls = Field()
	artists = Field()
	# artists_urls = Field()
	colors = Field()
	# colors_urls = Field()
	inks = Field()
	# inks_urls = Field()
	pencils = Field()
	# pencils_urls = Field()
	story_arc = Field()
	story_arc_url = Field()
	page_count = Field()
	print_release_date = Field()
	digital_release_date = Field()
	age_rating = Field() # FK
	sold_by = Field() #FK
	genre_names = Field() #FK
	genre_urls = Field() #FK
	genres = Field() #FK
	collected_edition_url = Field() # FK
	#is_collected_edition = False #BooleanField(default=False) -- not used?
	user_ratings_count = Field()
	user_star_rating = Field() #average star rating by users, rounded to whole numbers

	is_volume = Field() # is there a good chance this "issue" is a volume?

	# are these not used?
	summary = Field()
	cover_price = Field()
	volume = Field()

class CreatorItem(Item):
	# metadata fields
	scrape_site = Field()
	url = Field()
	type = Field()

	# regular fields
	name = Field()


class SeriesItem(Item):
	# metadata fields
	scrape_site = Field()
	url = Field()
	type = Field()

	# regular fields
	name = Field()

class PublisherItem(Item):
	# metadata fields
	scrape_site = Field()
	url = Field()
	type = Field()

	# regular fields
	name = Field()
	publisher_id = Field()

'''
class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    tags = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
'''


# class ModelItem(Item):
#     """
#     Make Peewee models easily turn into Scrapy Items.
#     >>> from models import Player
#     >>> item = ModelItem(Player())
#
#     https://gist.github.com/zachwill/00056d4304c58a035c87cdf5ff1e5e3e
#     """
#
#     def __init__(self, model, **kwds):
#         super(self.__class__, self).__init__()
#         self._model = model
#         for key in model._meta.fields.keys():
#             self.fields[key] = Field()
#         if kwds is not None:
#             for key, processor in kwds.items():
#                 self.fields[key] = Field(input_processor=MapCompose(
#                     strip_whitespace, processor
#                 ))
#
#     def __setitem__(self, key, value):
#         if key not in self.fields:
#             self.fields[key] = Field()
#         self._values[key] = value
#
#     def copy(self):
#         return copy.deepcopy(self)
#
#     @property
#     def model(self):
#         return self._model

# PeeweeIssueItem = ModelItem(ComixologyIssue())
# PeeweeCreatorItem = ModelItem(ComixologyCreator()) #m2m
# PeeweeCreatorIssueJunctionItem = ModelItem(ComixologyIssueCreatorJunction())
#
# PeeweeSeriesItem = ModelItem(ComixologySeries()) #m21
# PeeweeStoryArcItem = ModelItem(ComixologyStoryArc()) #m21
# PeeweePublisherItem = ModelItem(ComixologyPublisher()) #m21
# PeeweeGenreItem = ModelItem(ComixologyGenre()) #many to many
'''
# Extend the items; Items may use some fields that the database doesn't care about
class IssueItem(PeeweeIssueItem):
	#def __init__(self, n):
	#	super().__init__(n)
    testfield = Field()
#IssueItem = PeeweeIssueItem
CreatorItem = PeeweeCreatorItem
'''
