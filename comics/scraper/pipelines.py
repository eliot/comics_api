import json
from pprint import pprint
import itertools

from itemadapter import ItemAdapter

#from comics.config import db
from comics.models.scrape import ScrapeSite, ScrapeItem, ScrapeData
from comics.models.comixology import *
#from comics.constants import ScrapeSiteType, ComixologyScrapeItemTypes
from comics.config import db



class RawPostgresPipeline:
    '''Save raw scrape data to Postgres using Peewee. This data could be reprocessed later.'''

    def __init__(self, db_conn):
        self.db = db_conn

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            db_conn=crawler.settings.get('DATABASE')
        )

	# setup
    def open_spider(self, spider):
        # get database from spider
        pass #self.db = db

	# cleanup
    def close_spider(self, spider):
        pass

	# the primary work-doing callback
    def process_item(self, item, spider):
        print("ITEM")
        pprint(item)
        data = ItemAdapter(item).asdict()

		#item is a dict
        url = data['url']
        item_type = data['type']
        site_type = data['scrape_site']

        #prevent json serialization error
        #data['scrape_site'] = str(data['scrape_site'])

        # data = ItemAdapter(item).asdict()

        # delete these keys before we save to db
        data.pop('url', None)
        data.pop('type', None)
        data.pop('scrape_site', None)

        scrape_site, _ = ScrapeSite.get_or_create(name=str(site_type))

        with self.db.atomic():
            scrape_item = ScrapeItem.create(site=scrape_site, url=url)
            scrape_data = ScrapeData.create(item=scrape_item, data=dict(data))

        return item



class StructuredComixologyPostgresPipeline:
    '''Save structured Comixology.com data to Postgres using Peewee.'''

    def __init__(self, db_conn):
        self.db = db_conn

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            db_conn=crawler.settings.get('DATABASE')
        )

	# setup
    def open_spider(self, spider):
        # get database from spider
        pass #self.db = db

	# cleanup
    def close_spider(self, spider):
        pass

	# the primary work-doing callback
    def process_item(self, item, spider):
        # print("ITEM")
        # pprint(item)
        data = ItemAdapter(item).asdict()

		#item is a dict
        url = data['url']
        item_type = data['type']
        site_type = data['scrape_site']

        # delete metadata keys before we save to db
        data.pop('url', None)
        data.pop('type', None)
        data.pop('scrape_site', None)

        if isinstance(item, IssueItem): # use this way to check item types
        #if item_type is ComixologyScrapeItemTypes.ISSUE:
            print("type = ISSUE")

            # lookup issue first by primary key? ComixologyIssue.get()
            # issue, _ = ComixologyIssue.get_or_create(issue_id=data['issue_id'])
            issue = ComixologyIssue()

            issue.title = data['title']
            issue.issue_id = data['issue_id']
            issue.description = data['description']
            issue.price = data['price']
            sold_by, _ = ComixologyRefSoldBy.get_or_create(seller_name=data['sold_by'])
            issue.sold_by = sold_by
            age_rating, _ = ComixologyRefAgeRating.get_or_create(age_rating=data['age_rating'])
            issue.age_rating = age_rating
            collected_edition, _ = ComixologyIssue.get_or_create(url=data['collected_edition_url']) #???
            issue.collected_edition = collected_edition
        	# is_collected_edition = BooleanField(default=False)
        	issue.issue_number_end = data['issue_number_end']
        	issue.star_rating = data['user_star_rating']
        	issue.ratings_count = data['user_ratings_count']

        	# fields from base.Issue
        	issue.issue_number = data['issue_number']
        	issue.print_release_date = data['print_release_date']
        	issue.digital_release_date = data['digital_release_date']
        	issue.summary = data['description']
        	issue.cover_url = data['cover_url']
            # maybe make an ML model to scan covers and update these?
        	#issue.cover_price =
        	issue.page_count = data['page_count']

            publisher, _ = ComixologyPublisher.get_or_create(name=data['publisher'])
            issue.publisher = publisher

            # volume, _ = ComixologyIssue.get_or_create(name=data['series'])
            # issue.series = series

            series, _ = ComixologySeries.get_or_create(name=data['series'])
            issue.series = series

            # storyarc, _ = ComixologyStoryArc.get_or_create(name=data['series'])
            # issue.series = series

            # create all creators and many-to-many junction objects
            creatives = [('writer', t[0], t[1], i) for i, t in enumerate(data['writers'])] \
                + [('artist', t[0], t[1], i) for i, t in enumerate(data['artists'])] \
                + [('colors', t[0], t[1], i) for i, t in enumerate(data['colors'])] \
                + [('inks',   t[0], t[1], i) for i, t in enumerate(data['inks'])] \
                + [('pencils',t[0], t[1], i) for i, t in enumerate(data['pencils'])]

            for creator_role, creator_name, creator_url, creator_order in creatives:
                creative, _ = ComixologyCreator.get_or_create(name=creator_name)

                # these could be cached to eliminate database calls
                role = ComixologyRefCreatorRole.get_or_create(name=role_name)

                junction = ComixologyIssueCreatorJunction()
                junction.issue = issue
                junction.creator = creator
                junction.role = role
                junction.order = creator_order
                junction.create()

            issue.create()



        elif isinstance(item, SeriesItem):
            print("type = SERIES")
            series, _ = ComixologySeries.get_or_create(name=data['name'],
                            url=url, description=data['description'])

        elif isinstance(item, CreatorItem):
            print("type = CREATOR")
            creator, _ = ComixologyCreator.get_or_create(name=data['name'], url=url)

        elif isinstance(item, PublisherItem):
            print("type = PUBLISHER")
            creator, _ = ComixologyPublisher.get_or_create(name=data['name'], url=url)

        else:
            print("NO INSTANCE MATCH")
            print(data)



        # scrape_site, _ = ScrapeSite.get_or_create(name=str(site_type))
        #
        # with self.db.atomic():
        #     scrape_item = ScrapeItem.create(site=scrape_site, url=url)
        #     scrape_data = ScrapeData.create(item=scrape_item, data=dict(data))

        return item
