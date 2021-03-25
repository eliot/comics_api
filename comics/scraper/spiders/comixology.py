from scrapy.spiders import SitemapSpider
from scrapy import Request
from pprint import pprint as pp
from re import compile as re_compile

from comics.scraper.items import IssueItem, CreatorItem, SeriesItem#, GenreItem
from comics.utils.url import clean_url
from comics.config import db
from comics.constants import ScrapeSiteType, ComixologyScrapeItemTypes



class ComixologySpider(SitemapSpider):
    name = 'comixology'
    allowed_domains = ['comixology.com']
    download_delay = 2
    sitemap_urls = ['https://www.comixology.com/sitemap.xml']
    sitemap_rules = [
        ('\/digital-comic\/', 'parse_issue'),
        ('\/comics-creator\/', 'parse_creator'),
        # ('\/comics-publisher\/', 'parse_publisher'),
        ('\/comics-series\/', 'parse_series'),
        # ('\/comics-story-arc\/', 'parse_story_arc'),
        # ('\/comics-genre\/', 'parse_genre'),
        # https://www.comixology.com/Essential-Batman-Pt-1/bundle/1056 # bundles
    ]

    # for testing purposes
    custom_settings = {
        'DATABASE': db,
        'CLOSESPIDER_PAGECOUNT': 5
    }

    # used to grab the issue number
    re_issue_number = re_compile('\#([\d-]{0,6})')

    @staticmethod
    def clean_url(url):
        '''Remove url parameters'''
        return url.split('?')[0] if url else None


    def parse_issue(self, response):
        issue = {}

        issue['scrape_site'] = ScrapeSiteType.COMIXOLOGY
        issue['url'] = response.request.url
        issue['type'] = ComixologyScrapeItemTypes.ISSUE

        issue['issue_id'] = int(response.url.split('/')[-1].split('?')[0])
        issue['title'] = response.xpath('//*[@id="column2"]/h1/text()').get()

        issue['is_volume'] = "Volume" in issue['title'] or "Vol." in issue['title']

        # handle missing '#'
        # issue['issue_number'] = None
        # if len(issue['title'].split('#')) == 2:
        #     issue['issue_number'] = int(issue['title'].split('#')[1])

        issue['issue_number'] = None
        issue['issue_number_end'] = None

        # needs to handle missing '#' and double issues: '#28-29'
        issue_match = ComixologySpider.re_issue_number.search(issue['title'])

        if issue_match:
            # there is an issue number present (`#`)
            numbers = issue_match.group(1) # get the number without the `#` sign
            parts = numbers.split('-')

            # the beginning issue number
            issue['issue_number'] = int(parts[0])

            # get the ending issue number if applicable
            if len(parts) > 1:
                issue['issue_number_end'] = int(parts[1])

        # this may not be necessary to store
        issue['is_multi_issue'] = \
            True if issue['issue_number'] and issue['issue_number_end'] \
            else False

        # [Can an issue belong to more than one series? So far I haven't seen it.]
        issue['series'] = issue['title'].split('#')[0].strip()
        issue['series_url'] = response \
            .xpath('//*[@id="cmx_breadcrumb"]/a[3]/@href') \
            .get()
        # issue['series'] = list(zip(series, series_url))

        # handle series first (many to one foreign key)
        if issue['series_url']:
            yield Request(url=issue['series_url'], callback=self.parse_series)

        try:
            issue['price'] = float(
                response
                    .xpath('//h5[contains(@class, "item-price")]/text()')
                    .get()
                    .replace('$', '')
            )
        except ValueError:
            # the price = FREE
            issue['price'] = None

        issue['cover_url'] = response \
            .xpath('//*[@id="cover"]/img/@src').get()

        description = response.xpath('//*[@id="column2"]/section[@class="item-description"]/text()')
        # handle cases when there is no disclaimer field in the description
        if len(description) == 2:
            description = description[1].get()
        else:
            description = description.get()
        issue['description'] = description.strip()

        issue['publisher'] = response.xpath('normalize-space(//*[@id="column3"]/div[@class="credits"]/div[@class="publisher"]/a[2]/h3/text())').get()
        issue['publisher_url'] = response.xpath('//*[@id="column3"]/div[@class="credits"]/div[@class="publisher"]/a[2]/@href').get()

        writers = list(map(str.strip,
                            response.xpath('//h2[@title="Written by"]/a/text()').getall()
                         ))
        writers_urls = response.xpath('//h2[@title="Written by"]/a/@href').getall()
        issue['writers'] = list(zip(writers, writers_urls))
        # how do we model author ordering? zip(range(1, len(writers)), (issue['writers'], issue['writer_urls']))

        artists = list(map(str.strip,
                            response.xpath('//h2[@title="Art by"]/a/text()').getall()
                         ))
        artists_urls = response.xpath('//h2[@title="Art by"]/a/@href').getall()
        issue['artists'] = list(zip(artists, artists_urls))
        # TODO: handle artist/creator ORDERING on issue basis

        # colors ("Colored by")
        colors = list(map(str.strip,
                            response.xpath('//h2[@title="Colored by"]/a/text()').getall()
                         ))
        colors_urls = response.xpath('//h2[@title="Colored by"]/a/@href').getall()
        issue['colors'] = list(zip(colors, colors_urls))

        # inks ("Inks")
        inks_names = list(map(str.strip,
                            response.xpath('//h2[@title="Inks"]/a/text()').getall()
                         ))
        inks_urls = response.xpath('//h2[@title="Inks"]/a/@href').getall()
        issue['inks'] = list(zip(inks_names, inks_urls))

        # pencils
        pencils_names = list(map(str.strip,
                            response.xpath('//h2[@title="Pencils"]/a/text()').getall()
                         ))
        pencils_urls = response.xpath('//h2[@title="Pencils"]/a/@href').getall()
        issue['pencils'] = list(zip(pencils_names, pencils_urls))

        # handle all creators before issues
        for url in (
            writers_urls+
            artists_urls +
            colors_urls +
            inks_urls +
            pencils_urls):
            yield Request(url=url, callback=self.parse_creator)

        issue['story_arc'] = response.xpath('normalize-space(//*[@id="column3"]/div[@class="credits"]/div[contains(text(), \'Story Arc\')]/following-sibling::a/text())').get()
        issue['story_arc_url'] = response.xpath('//*[@id="column3"]/div[@class="credits"]/div[contains(text(), \'Story Arc\')]/following-sibling::a/@href').get()

        # handle story arcs first
        # if issue['story_arc_url']:
        #     yield Request(url=issue['story_arc_url'], callback=self.parse_story_arc)

        issue['page_count'] = int(response.xpath('//h4[contains(text(), \'Page Count\')]/following-sibling::div[@class="aboutText"]/text()').get().split()[0])
        issue['print_release_date'] = response.xpath('//h4[contains(text(), \'Print Release Date\')]/following-sibling::div[@class="aboutText"]/text()').get()
        issue['digital_release_date'] = response.xpath('//h4[contains(text(), \'Digital Release Date\')]/following-sibling::div[@class="aboutText"]/text()').get()

        # could be a ref table AgeRating()
        issue['age_rating'] = response.xpath('normalize-space(//h4[contains(text(), \'Age Rating\')]/following-sibling::div[@class="aboutText"]/text())').get()

        # could be a ref table Seller()
        issue['sold_by'] = response.xpath('//h4[contains(text(), \'Sold by\')]/following-sibling::div[@class="aboutText"]/text()').get()


        issue['genre_names'] = response.xpath('//div[@class="credits"]/div[contains(text(), \'Genres\')]/following-sibling::a[contains(@href, \'comics-genre\')]/text()').getall()
        issue['genre_names'] = list(map(str.strip, issue['genre_names']))
        issue['genre_urls'] = response.xpath('//div[@class="credits"]/div[contains(text(), \'Genres\')]/following-sibling::a[contains(@href, \'comics-genre\')]/@href').getall()
        issue['genres'] = list(zip(issue['genre_names'], issue['genre_urls'])) # turn the genres into name + url pairs

        # handle genres first
        # for url in issue['genre_urls']:
        #     yield Request(url=url, callback=self.parse_genre)

        # If this has a value, then it is part of a collected edition. The collected edition is itself an issue.
        issue['collected_edition_url'] = response.xpath('//*[@class="collectedEdition"]/div[contains(text(), \'collected edition\')]/following-sibling::a/@href').get()
        # yield the collected edition - this must be done to make sure we can link to the issue later
        if issue['collected_edition_url']:
            yield Request(url=issue['collected_edition_url'], callback=self.parse_issue)
        # handle collected editions first
        # if issue['collected_edition_url']:
        #     yield Request(url=issue['collected_edition_url'], callback=self.parse_issue)
        user_ratings_count = response.xpath('//div[@itemprop="reviewCount"]/text()').get()
        # sample from above variable: `Average Rating (319):`
        # needs additional processing
        issue['user_ratings_count'] = user_ratings_count
        issue['user_star_rating'] = int(response.xpath('//div[@class="rating-total hidden"]/text()').get())

        yield IssueItem(issue)
        #yield(issue)

    def parse_creator(self, response):
        '''Parse a creator page. These pages do not have descriptions. Example page: https://www.comixology.com/Alan-Moore/comics-creator/2692'''
        creator = {}

        creator['scrape_site'] = ScrapeSiteType.COMIXOLOGY
        creator['url'] = self.clean_url(response.url) #response.request.url
        creator['type'] = ComixologyScrapeItemTypes.CREATOR

        creator['name'] = response.xpath('normalize-space(//*[@id="cmx_breadcrumb"]/h2/text())').get()

        yield CreatorItem(creator)

    # def parse_genre(self, response):
    #     genre = {}
    #     genre['name'] = response.xpath('normalize-space(//*[@id="cmx_breadcrumb"]/h2/text())').get()
    #     genre['url'] = self.clean_url(response.url)
    #     yield genre

    def parse_publisher(self, response):
        '''Parse a publisher page. These pages do not have descriptions. Example page: https://www.comixology.com/DC/comics-publisher/1-0'''
        publisher = {}
        publisher['name'] = response.xpath('normalize-space(//*[@id="cmx_breadcrumb"]/h2/text())').get()
        publisher['url'] = self.clean_url(response.url)
        publisher['publisher_id'] = int(response.url.split('/')[-1].split('?')[0])
        yield publisher

    # def parse_story_arc(self, response):
    #     story_arc = {}
    #     story_arc['name'] = response.xpath('normalize-space(//*[@id="cmx_breadcrumb"]/h2/text())').get()
    #     story_arc['url'] = self.clean_url(response.url)
    #     yield story_arc
    #
    def parse_series(self, response):
        '''Parse a series page. Example: https://www.comixology.com/Invincible/comics-series/684?ref=Y29taWMvdmlldy9kZXNrdG9wL2JyZWFkY3J1bWJz'''
        series = {}

        # pipeline setup
        series['scrape_site'] = ScrapeSiteType.COMIXOLOGY
        series['url'] = self.clean_url(response.url) #response.request.url
        series['type'] = ComixologyScrapeItemTypes.SERIES

        # TODO: check diff between response.url and response.request.url

        series['name'] = response.xpath('normalize-space(//*[@id="cmx_breadcrumb"]/h2/text())').get()
        series['description'] = response.xpath('//div[@itemprop="description"]/text()').get()

        yield SeriesItem(series)
