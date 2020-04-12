# -*- coding: utf-8 -*-

import copy
from scrapy import Item, Field

from ..models.comixology import *
'''
class GenericItem(Item):
	date_scraped = DateTimeField(datetime.now, default=datetime.now)
	url = CharField(primary_key=True) 
	title = CharField()
	description = TextField()

class Issue(GenericItem):
	
'''
class ModelItem(Item):
    """
    Make Peewee models easily turn into Scrapy Items.
    >>> from models import Player
    >>> item = ModelItem(Player())

    https://gist.github.com/zachwill/00056d4304c58a035c87cdf5ff1e5e3e
    """

    def __init__(self, model, **kwds):
        super(self.__class__, self).__init__()
        self._model = model
        for key in model._meta.fields.keys():
            self.fields[key] = Field()
        if kwds is not None:
            for key, processor in kwds.items():
                self.fields[key] = Field(input_processor=MapCompose(
                    strip_whitespace, processor
                ))

    def __setitem__(self, key, value):
        if key not in self.fields:
            self.fields[key] = Field()
        self._values[key] = value

    def copy(self):
        return copy.deepcopy(self)

    @property
    def model(self):
        return self._model

PeeweeIssueItem = ModelItem(ComixologyIssue())
PeeweeCreatorItem = ModelItem(ComixologyCreator()) #m2m
PeeweeCreatorIssueJunctionItem = ModelItem(ComixologyIssueCreatorJunction())

PeeweeSeriesItem = ModelItem(ComixologySeries()) #m21
PeeweeStoryArcItem = ModelItem(ComixologyStoryArc()) #m21
PeeweePublisherItem = ModelItem(ComixologyPublisher()) #m21
PeeweeGenreItem = ModelItem(ComixologyGenre()) #many to many
'''
# Extend the items; Items may use some fields that the database doesn't care about
class IssueItem(PeeweeIssueItem):
	#def __init__(self, n):
	#	super().__init__(n)
    testfield = Field()
#IssueItem = PeeweeIssueItem
CreatorItem = PeeweeCreatorItem
'''
